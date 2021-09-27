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
    digitID = db.Column(db.Integer, primary_key=True, unique=True)  
    # username of the account
    userName = db.Column(db.String(80), unique=True, nullable=False)  
    # shipping address of the user
    shipAddress = db.Column(db.String(64), nullable=False)
    # products in shopping cart  
    shoppingCart = db.Column(db.String(500), nullable=True)
    # shipping period of the products 
    # there is 4 period, use 1 to 4 represent period
    shipPeriod = db.Column(db.Integer, nullable=False)
    # gift cards, coupons
    giftCard = db.Column(db.String(64), nullable=True)
    # subtotal of staffs in shopping cart
    subtotal = db.Column(db.Float, nullable=False)
    #tax of all products in shopping cart
    tax = db.Column(db.Float, nullable=False)
    #shipping fee of the package
    shipFee = db.Column(db.Float, nullable=False)
    # total cost of all products
    billAmount = db.Column(db.Float, nullable=False)  
    # ship status of the package
    shipStatus = db.Column(db.String(64), nullable=False)
    # track number of the package
    trackNum = db.Column(db.String(64), nullable=False)
    # name of shipping company
    courierName = db.Column(db.String(80), nullable=False)



    def __repr__(self):
        return '<User %r>' % self.userName