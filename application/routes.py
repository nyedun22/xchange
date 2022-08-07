from flask import render_template, request, flash
from __init__ import app  # db
from forms import CustomerRegistrationForm, LoginForm, CurrencyForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


# route for currency convertor
@app.route('/currency')
def currency_convertor():
    form = CurrencyForm()
    # all_currencies = get_currencies()
    return render_template('currency.html', form=form)   # , all_currencies=all_currencies


# route for user sign up form
@app.route('/register', methods=['GET', 'POST'])
def user_sign_up():
    form = CustomerRegistrationForm()
    # validation for new customer registration form
    if request.method == 'POST':
        username = request.form['username'],
        password = request.form['password'],
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        email = request.form['email'],
        address_line_one = request.form['address'],
        postcode = request.form['postcode']

        # _connect_to_db()
        # user = Bank_User()
        # user.create_account(first_name=first_name[0], last_name=last_name[0], username=username[0], email=email[0], pass_word=password[0], address_line_1=address_line_one[0], postcode=postcode)

        """if/else statement - if form field input text length less than required user will get error
        otherwise user data will submit to database tables"""
        if len(first_name) == 0 \
                or len(last_name) == 0 \
                or len(email) == 0\
                or len(address_line_one) == 0\
                or len(postcode) == 0\
                or len(password) < 4\
                or len(username) == 0:
            error = "Please complete each section of this form"
            return render_template('home.html', title='Home', form=form)
        return render_template('register.html', title='Register', form=form)  # message=error

        # mydb.user_login = user_sign_up(
        #     username=username,
        #     pass_word=password)
        #
        # mydb.user_details = user_sign_up(
        #     first_name=first_name,
        #     last_name=last_name,
        #     email=email,
        #     address=address_line_one,
        #     postcode=postcode,
        #     user_login=user_login)
        #
        # # cur = mysql.connection.cursor()
        # mydb.session.add(user_login)
        # mydb.session.add(user_sign_up)
        # mydb.session.commit()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
    else:
        return render_template('register.html', form=form)


# route for user login form
@app.route('/login')
def user_login():
    form = LoginForm()
    # user = Bank_User()

    return render_template('login.html', form=form)


# route for viewing transactions page
@app.route('/transactions')
def transactions():
    return render_template('transactions.html')
