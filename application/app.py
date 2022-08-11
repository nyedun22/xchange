from db_models import user_details, bank_details, foreign_account
from flask import Flask, render_template, request, flash, redirect, url_for
from forms import CustomerRegistrationForm, LoginForm, CurrencyForm, TransactionForm
from sqlalchemy.orm import Session
from __init__ import create_app, db
from functions import new_balance, hash_password

session = Session()
app = create_app()

# setting our global variables
GBP_amount = 0
bank_user_id = None

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
            if str(user.pass_word) == str(input_password):
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

        pwd = hash_password(password[0])
        f_n = first_name[0]
        l_n = last_name[0]
        em = email[0]
        addr = address[0]
        pc = postcode
        urnm = username[0]

        new_user_details = user_details(first_name=f_n, last_name=l_n, email=em, address_line_1=addr, postcode=pc,
                                        username=urnm, pass_word=pwd)

        db.session.add(new_user_details)
        db.session.commit()

        user = user_details.query.filter_by(username=username[0]).first()
        new_user_id = user.user_id
        new_user_bank = bank_details(user_id=new_user_id, sort_code=105010, main_account_balance=1000)
        db.session.add(new_user_bank)
        db.session.commit()

        flash(f'Account created for {form.username.data}! You now have an account containing £1000', category='success')
        return redirect(url_for('user_login'))

    return render_template('register.html', form=form)


# route for currency convertor
@app.route('/currency',  methods=['GET', 'POST'])
def currency_convertor():
    form = CurrencyForm()
    if request.method == 'POST' and form.validate():
        gbp = request.form['gbp'],
        dropdown = request.form['dropdown']

        global GBP_amount
        GBP_amount = gbp[0]

        return redirect(url_for('transactions', gbp_code=gbp, dropdown_code=dropdown))

    return render_template('currency.html', form=form)

@app.route('/transactions', methods=['GET', 'POST'])
def transactions():
    form = TransactionForm()
    gbp_code = request.args.get('gbp_code')
    dropdown_code = request.args.get('dropdown_code')


     ##at the moment this runs before the transaction is accepted
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
            foreign_account_details = foreign_account(account_number=account_number, foreign_account_balance=300, foreign_currency=dropdown_code )
            db.session.add(foreign_account_details)
            db.session.commit()

            flash('Transaction successful.', category='success')

        #return {new_account_balance : bank_user_id}
    return render_template('transactions.html', form=form)

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True, port=5006)
