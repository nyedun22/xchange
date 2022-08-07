#from application import app
# import the ./application/routes.py file
#from application import routes
from db_models import user_details
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_migrate import Migrate
from forms import CustomerRegistrationForm, LoginForm, CurrencyForm
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash
# from flask_login import (
#     UserMixin,
#     login_user,
#     LoginManager,
#     current_user,
#     logout_user,
#     login_required,
# )
#
# login_manager = LoginManager()
# login_manager.session_protection = "strong"
# login_manager.login_view = "login"
# login_manager.login_message_category = "info"

session = Session()
db = SQLAlchemy()
# migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    app.secret_key = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    #login_manager.init_app(app)
    db.init_app(app)
    #migrate.init_app(app, db)
    bcrypt.init_app(app)

    return app

app = create_app()

# Home route
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

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
                #login_user(user)
                return redirect(url_for('currency_convertor'))
            else:
                raise Exception
        except:
            return render_template('login.html', form=form)

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

        #secure_password = bcrypt.generate_password_hash(password[0])

        new_user_details = user_details(first_name=first_name[0], last_name=last_name[0], email=email[0],
                                        address_line_1=address[0], postcode=postcode, username=username[0], pass_word=password[0])
        db.session.add(new_user_details)
        db.session.commit()
        return redirect(url_for('user_login'))

    return render_template('register.html', form=form)
        # """if/else statement - if form field input text length less than required user will get error
        # otherwise user data will submit to database tables"""
        # if len(first_name) == 0 \
        #         or len(last_name) == 0 \
        #         or len(email) == 0\
        #         or len(address) == 0\
        #         or len(postcode) == 0\
        #         or len(password) < 4\
        #         or len(username) == 0:
        #     error = "Please complete each section of this form"
        #     return render_template('home.html', title='Home', form=form)
        #return render_template('register.html', title='Register', form=form)  # message=error
    #
    # if form.validate():
    #     flash(f'Account created for {form.username.data}!', 'success')

    # else:
    #     return render_template('register.html', form=form)


# route for currency convertor
@app.route('/currency')
def currency_convertor():
    form = CurrencyForm()
    # all_currencies = get_currencies()
    return render_template('currency.html', form=form)   # , all_currencies=all_currencies

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True, port=5006)