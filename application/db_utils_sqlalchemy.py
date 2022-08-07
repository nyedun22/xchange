# import sqlalchemy as db
# import pymysql
#
# def create_user_details(first_name, last_name, email, address, postcode):
#     engine = db.create_engine('sqlite:///site.db')
#     connection = engine.connect()
#     metadata = db.MetaData()
#     user_details = db.Table('user_details', metadata, autoload=True, autoload_with=engine)
#     query = db.insert(user_details).values(first_name=first_name, last_name=last_name, email=email, address_line_1=address, postcode=postcode)
#     ResultProxy = connection.execute(query)
#
# def create_login(user_id, username, password):
#     engine = db.create_engine('sqlite:///site.db')
#     connection = engine.connect()
#     metadata = db.MetaData()
#     user_login = db.Table('user_login', metadata, autoload=True, autoload_with=engine)
#     query = db.insert(user_login).values(user_id = user_id, username=username, pass_word=password)
#     ResultProxy = connection.execute(query)

    # def verify_login(self, username_input, password_input):
    #     connect_to_db()
    #     project_db = db.Table('user_details', metadata, autoload=True, autoload_with=engine)
    #     query = db.select([project_db]).where(project_db.columns.username == username_input)
    #     ResultProxy = connection.execute(query)
    #     ResultSet = ResultProxy.fetchall()




#create_user_details('Jeff', 'Rogers', 'jeffrog@live.com', '450 Pudding lane', 'SE1 9PJ')
#create_login(5, 'Jeffrog', 'rogershouse')


from db_models import user_details
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from forms import CustomerRegistrationForm, LoginForm, CurrencyForm
from sqlalchemy.orm import Session
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

session = Session()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    app.secret_key = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    return app

app = create_app()
input_username = ('MariaS', 0)
@app.route('/')
def learning():
    user = db.session.query(user_details.username).filter_by(username=input_username[0]).first()
    password = db.session.query(user_details.pass_word).filter_by(username=input_username[0]).first()
    #if db_username[0][0] == 'MariaS' and db_password[0][0] == 'Iamsotired':
    return {str(user[0]): str(password[0]) }
    #return {'no ': 'match'}


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True, port=5007)