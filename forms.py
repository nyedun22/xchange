from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms_sqlalchemy.fields import QuerySelectField
from db_models import currency_codes
from countries import formatted_list



# customer registration form
class CustomerRegistrationForm(FlaskForm):
    # user login elements
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message="Passwords must match")])

    # user_details elements
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email(message='Please supply a valid email')])
    address = StringField('Address Line 1', validators=[DataRequired()])
    postcode = StringField('Postcode', validators=[DataRequired()])
    # # submit
    submit = SubmitField('Sign Up')


# customer login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(message='Please supply a valid email')])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


# currency form
class CurrencyForm(FlaskForm):
    gbp = DecimalField('How much money would you like to exchange?')
    dropdown = SelectField('Select your currency', choices=formatted_list, validators=[DataRequired()])
    submit = SubmitField("Buy currency!")