from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import SQL packages

# Create a Flask application object and set the URI for
# the database to initiate connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# Set to False otherwise it adds significant overhead in the future
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Use the application object as a parameter to create
# an object of class SQLAlchemy
class User(db.Model):
    # These are the attributes required by the user/customers/stakeholders
    # the primary key in the table
    digitID = db.Column(db.Integer, primary_key=True)
    # username of the account
    userName = db.Column(db.String(80), unique=True, nullable=False)
    # password of the account
    password = db.Column(db.String(64), nullable=False)
    # The real name of the user
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    # user's age, not mandatory
    userAge = db.Column(db.Integer)
    # user's rate star based on other users' review, not mandatory
    userRateStar = db.Column(db.Integer)
    # email address of the user
    email = db.Column(db.String(120), unique=True, nullable=False)
    # user's phone number, not mandatory
    userPhone = db.Column(db.Integer)
    billingAddress = db.Column(db.String(160), nullable=False)  # user address
    # postal code associated with the address
    postalCode = db.Column(db.String(160), nullable=False)
    # if the user is an enterprise seller
    isEnterpriseSeller = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.userName
