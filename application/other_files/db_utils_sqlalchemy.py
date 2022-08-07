# import sqlalchemy as db
# import pymysql

# def create_account(first_name, last_name, username, email, password, address, postcode):
#     engine = db.create_engine('mysql+pymysql://root:password@localhost:3306/exchange_project')
#     connection = engine.connect()
#     metadata = db.MetaData()
#     project_db = db.Table('user_details', metadata, autoload=True, autoload_with=engine)
#     query = db.insert(project_db).values(first_name=first_name, last_name=last_name, username=username, email=email, pass_word=password, address_line_1=address, postcode=postcode)
#     ResultProxy = connection.execute(query)


    # def verify_login(self, username_input, password_input):
    #     connect_to_db()
    #     project_db = db.Table('user_details', metadata, autoload=True, autoload_with=engine)
    #     query = db.select([project_db]).where(project_db.columns.username == username_input)
    #     ResultProxy = connection.execute(query)
    #     ResultSet = ResultProxy.fetchall()




#create_account('Alan', 'Smash', 'AlanS', 'alan@live.com', 'alanrules', '53 lane', '3282')
