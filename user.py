from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import SQL packages

# Create a Flask application object and set the URI for the database to initiate connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# Set to False otherwise it adds significant overhead in the future
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Use the application object as a parameter to create an object of class SQLAlchemy
class User(db.Model):
    # These are the attributes required by the user/customers/stakeholders
    digitID = db.Column(db.Integer, primary_key=True)  # the primary key in the table
    userName = db.Column(db.String(80), unique=True, nullable=False)  # username of the account
    password = db.Column(db.String(64), nullable=False)  # password of the account
    firstName = db.Column(db.String(80), nullable=False)  # The real name of the user
    lastName = db.Column(db.String(80), nullable=False)
    userAge = db.Column(db.Integer)  # user's age, not mandatory
    userRateStar = db.Column(db.Integer)  # user's rate star based on other users' review, not mandatory
    email = db.Column(db.String(120), unique=True, nullable=False)  # email address of the user
    userPhone = db.Column(db.Integer)  # user's phone number, not mandatory
    billingAddress = db.Column(db.String(160), nullable=False)  # user address
    postalCode = db.Column(db.String(160), nullable=False)  # postal code associated with the address
    isEnterpriseSeller = db.Column(db.Boolean, nullable=False)  # if the user is an enterprise seller

    def __repr__(self):
        return '<User %r>' % self.userName