"""
Import Flask and SQLAlchemy
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define a Flask entity as app
app = Flask(__name__)
# Configure app with SQL database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
# Disable Mod Tracking to avoid significant overheard error
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Create a global variable for interacting with the database
db = SQLAlchemy(app)

"""
Product Class Data Model
"""


class Product(db.Model):
    # product ID which will be the key by which all other data can be found
    product_id = db.Column(db.Integer, primary_key=True)
    # product name which is mandatory, max 80 chars aligning with eBay
    name = db.Column(db.String(80), nullable=False)
    # condition of the product which is mandatory, max 60 chars
    # **maybe should be selection not string?**
    condition = db.Column(db.String(60), nullable=False)
    # seller of the product which is mandatory, and must be a unique string,
    # max 50 chars
    seller = db.Column(db.String(50), unique=True, nullable=False)
    # model # of the product which not mandatory
    modelNum = db.Column(db.Integer)
    # colour of the product which is mandatory, max 40 chars
    colour = db.Column(db.String(40), nullable=False)
    # category of the product which is mandatory, max 60 chars
    # **maybe should be selection not string?**
    category = db.Column(db.String(60), nullable=False)
    # product description which is mandatory, max 1500 chars
    description = db.Column(db.String(1500), nullable=False)

    def __repr__(self):
        # printable version of product which returns the product identifier
        return '<Product %r>' % self.product_id
