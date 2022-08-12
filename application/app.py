from db_models import user_details, bank_details, foreign_account, transactions_record
from flask import Flask, render_template, request, flash, redirect, url_for
from forms import CustomerRegistrationForm, LoginForm, CurrencyForm, TransactionForm
from sqlalchemy.orm import Session
from __init__ import create_app, db
from functions import new_balance, hash_password
from api_file import Currency


session = Session()
app = create_app()

# setting our global variables to updating in functions
GBP_amount = 0
bank_user_id = None
currency_rate = None
foreign_amount = 0
dropdown_code = None

# Home route
@app.route('/')
@app.route('/home')
def home():
    return render_template('home_not_logged_in.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def user_login():
    form = LoginForm()
    if request.method == 'POST':
        input_username = request.form.get('username'),
        input_password = request.form.get('password')

        try:
            user = user_details.query.filter_by(username=input_username[0]).first()
            secure_password = hash_password(input_password)
            if user.pass_word == secure_password:
                flash('Login successful.', category='success')
            else:
                raise Exception
        except:
            flash('Incorrect username or password, please try again.', category='error')
            return render_template('login.html', form=form)
        else:
            global bank_user_id
            bank_user_id = int(user.user_id)
            return redirect(url_for('currency_convertor'))

    return render_template('login.html', form=form)

# Register route
@app.route('/register', methods=['GET', 'POST'])
def user_sign_up():
    form = CustomerRegistrationForm()
    # validation for new customer registration form
    if request.method == 'POST' and form.validate():
        username = request.form['username'],
        password = request.form['password'],
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        email = request.form['email'],
        address = request.form['address'],
        postcode = request.form['postcode']

        hashed_password = hash_password(password[0])

        try:
            new_user_details = user_details(first_name=first_name[0], last_name=last_name[0], email=email[0], address_line_1=address[0], postcode=postcode[0],
                                            username=username[0], pass_word=hashed_password)
            db.session.add(new_user_details)
            db.session.commit()

        except:
            flash('Error creating user! Email and/or username already exists please try again', category='error')

        else:
            user = user_details.query.filter_by(username=username[0]).first()
            new_user_id = user.user_id
            new_user_bank = bank_details(user_id=new_user_id, sort_code=105010, main_account_balance=1000)
            db.session.add(new_user_bank)
            db.session.commit()

            flash(f'Account created for {form.username.data}! You now have an account containing £1000',
                  category='success')
            return redirect(url_for('user_login'))
        finally:
            pass


    return render_template('register.html', form=form)


# route for currency convertor
@app.route('/currency',  methods=['GET', 'POST'])
def currency_convertor():
    form = CurrencyForm()
    if request.method == 'POST' and form.validate():
        gbp = request.form['gbp'],
        dropdown = request.form['dropdown']

        global GBP_amount
        GBP_amount = int(gbp[0])

        return redirect(url_for('transactions', gbp_code=gbp, dropdown_code=dropdown))

    return render_template('currency.html', form=form)

# Route to proceed with transation
@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    form = TransactionForm()
    gbp_code = request.args.get('gbp_code')
    global dropdown_code
    dropdown_code = request.args.get('dropdown_code')

    #linking to API and updating global variables
    global currency_rate
    global foreign_amount
    c = Currency()
    currency_rate = c.get_rate(dropdown_code)
    foreign_amount = c.exchange_amount(GBP_amount)

    return render_template('transactions.html', value = gbp_code, value1 = foreign_amount, value2= dropdown_code, value3 = currency_rate, form=form)

# Route to successful checked out transaction
@app.route('/checkout')
def checkout():
    form = TransactionForm()
    try:
        global bank_user_id
        if bank_user_id is None:
            raise Exception
    except:
        flash('Error with processing transaction please log back in!', category='error')
        return redirect(url_for('user_login'))
    else:
        try:
            bank_user = bank_details.query.filter_by(user_id=bank_user_id).first()
            bank_balance = bank_user.main_account_balance
            if int(bank_balance) < int(GBP_amount):
                raise Exception
        except:
            flash('Not enough funds in your account to support transaction, you will now be logged out!', category='error')
            return redirect(url_for('user_login'))
        else:
            #updating current account with new balance post transaction
            new_account_balance = new_balance(bank_balance, GBP_amount)
            db.session.query(bank_details).filter(bank_details.user_id == bank_user_id).update(
                {'main_account_balance': new_account_balance})

            #link to foreign account using account number
            account_number = bank_user.account_number
            foreign_account_details = foreign_account(account_number=account_number, foreign_account_balance=foreign_amount, foreign_currency=dropdown_code)
            db.session.add(foreign_account_details)
            db.session.commit()

            #recording transaction
            foreign_details = foreign_account.query.filter_by(account_number=account_number).first()
            foreign_account_number = foreign_details.foreign_account_number
            transaction_record = transactions_record(foreign_account_number=foreign_account_number, account_number=account_number, foreign_currency=dropdown_code, gbp_amount=GBP_amount, foreign_currency_amount=foreign_amount, exchange_rate=currency_rate)
            db.session.add(transaction_record)
            db.session.commit()

            flash('Transaction successful.', category='success')
        finally:
            pass

    return render_template('success.html', form=form)

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True, port=5006)
