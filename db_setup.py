from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column,String,DateTime,Integer, create_engine
from datetime import datetime
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

connection_string="sqlite:///"+os.path.join(BASE_DIR, 'site.db')

Base=declarative_base()

engine=create_engine(connection_string,echo=True)

Session=sessionmaker()

"""
class user_details
    user_ID int
    first_name str
    last_name str
    username str
    email str
    pass_word str
    address_line_1 str
    postcode str
"""
class user_details(Base):
    __tablename__='user_details'
    user_ID=Column(Integer(),primary_key=True, nullable=False)
    first_name=Column(String(15), nullable=False)
    last_name=Column(String(15), nullable=False)
    username=Column(String(20), nullable=False,unique=True)
    email=Column(String(80), unique=True,nullable=False)
    pass_word=Column(String(20), nullable=False)
    address_line_1=Column(String(50), nullable=False)
    postcode=Column(String(7),nullable=False)

    def __repr__(self):
        return f"<user_details user_ID={self.user_ID} first_name={self.first_name} last_name={self.last_name} username={self.username} email={self.email} pass_word={self.pass_word} address_line_1={self.address_line_1} postcode={self.postcode}"

new_users=user_details(user_ID=1, first_name='John', last_name='Smith', username='JohnS', email="john@smith.com", pass_word="asdfghi", address_line_1="87 Mill Road", postcode="RH158DY")
