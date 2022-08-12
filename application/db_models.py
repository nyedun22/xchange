from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345678"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class user_details(db.Model):
    __tablename__ = "user_details"
    user_id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    address_line_1 = db.Column(db.String(50), nullable=False)
    postcode = db.Column(db.String(7), nullable=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    pass_word= db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"user_details('{self.user_id}', '{self.first_name}', '{self.last_name}', '{self.email}', '{self.address_line_1}', '{self.postcode}', '{self.username}', '{self.pass_word}')"
        

class bank_details(db.Model):
    __tablename__ = "bank_details"
    account_number = db.Column(db.Integer(), nullable=False, primary_key=True, unique=True)
    user_id = db.Column(db.Integer, ForeignKey('user_details.user_id'), nullable=False)
    sort_code = db.Column(db.Integer(), nullable=False)
    main_account_balance = db.Column(db.Numeric, nullable=False)

    def __repr__(self):
        return f"bank_details('{self.account_number}', '{self.user_id}', '{self.sort_code}', '{self.main_account_balance}')"


class foreign_account(db.Model):
    __tablename__ = "foreign_account"
    foreign_account_number = db.Column(db.Integer(), nullable=False, primary_key=True, unique=True)
    account_number = db.Column(db.Integer(), ForeignKey('bank_details.account_number'), nullable=False)
    foreign_account_balance = db.Column(db.Numeric, nullable=False)
    foreign_currency = db.Column(db.String(3), nullable=False)

    def __repr__(self):
        return f"foreign_account('{self.foreign_account_number}', '{self.account_number}', '{self.foreign_account_balance}', '{self.foreign_currency}')"


class transactions_record(db.Model):
    __tablename__ = "transactions_record"
    transaction_ID = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    foreign_account_number = db.Column(db.Integer(), ForeignKey('foreign_account.foreign_account_number'),
                                       nullable=False)
    account_number = db.Column(db.Integer(), ForeignKey('bank_details.account_number'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    foreign_currency = db.Column(db.String(3), nullable=False)
    gbp_amount = db.Column(db.Numeric, nullable=False)
    foreign_currency_amount = db.Column(db.Numeric, nullable=False)
    exchange_rate = db.Column(db.Numeric, nullable=False)

    def __repr__(self):
        return f"(transactions_record'{self.transaction_ID}','{self.foreign_account_number}', '{self.account_number}', '{self.date}', '{self.foreign_currency}', '{self.gbp_amount}', '{self.foreign_currency_amount}', '{self.exchange_rate}')"


class currency_codes(db.Model):
    __tablename__ = "currency_codes"
    currency_three_letters = db.Column(db.String(3), primary_key=True, nullable=False)
    currency_name = db.Column(db.String(30), nullable=False)
    country = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"currency_codes('{self.currency_three_letters}', '{self.currency_name}', '{self.country}')"


db.create_all()