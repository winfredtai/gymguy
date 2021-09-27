from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import SQL packages

# Create a Flask application object and set the URI for the database to initiate connection
app = Flask(__name__)
# Connect flask to a database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# Set to False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Use the application object as a parameter to create an object of class SQLAlchemy
class Transcation(db.Model):
    # These are the attributes required
    # the primary key in the table
    digitID = db.Column(db.Integer, primary_key=True)  
    # username of the account
    userName = db.Column(db.String(80), unique=True, nullable=False)  
    # shipping address of the user
    shipAddress = db.Column(db.String(64), unique=True, nullable=False)
    # The account balance of the user
    accountBalance = db.Column(db.Integer, unique=True)  
    # total cost of all products
    totalBill = db.Column(db.Integer, unique=True)  


    def __repr__(self):
        return '<User %r>' % self.userName