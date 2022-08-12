Project title: Xchange

Project description: we have built a banking website that allows users to create an account to exchange their pounds into a currency of their choice. Once the user has created an account, they will access a login page. All users are given £1000 as their starting balance. Afterwards, they will select the GBP amount they want to exchange and their target currency in a dropdown menu. Soon after that, our website will show the exchange rate to the user, who can accept it or decline it. If the user accepts it, they will be taken to a confirmation page. If they decline the conversion, they will be logged out and no funds will be taken out from their accounts.

Modules that need to be imported to run the project:

    flask
    flask_sqlalchemy
    flask_wtf
    wtforms
    wtforms.validators
    wtforms_sqlalchemy
    flask_bcrypt
    flask_migrate
    datetime
    hashlib
    
Running the project:

First, go to the directory application and run db_models.py to create the database (site.db). Optionally, db_dummy_data_insert.py can be run to populate the database with dummy info.
Afterwards, run app.py to initiate the Flask server.
Then, you can create an account and login with the details you have provided.
At the end, you can open the database using software such as DBBrowser(SQLite) to see the tables now populated with the information provided by the user. 

Credits:
Juliette Behr
Gianne Nandra
Brenda Murage
Natasha Edun
Aurora Sanchez Diaz
CFG Nanodegree - July/August 2022
