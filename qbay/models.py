from qbay import app
from flask_sqlalchemy import SQLAlchemy


'''
This file defines data models and related business logics
'''


db = SQLAlchemy(app)



class User(db.Model):
    username = db.Column(
        db.String(80), nullable=False)
    # user is uniquely identified by his/her email address
    email = db.Column(
        db.String(120), unique=True, nullable=False,
        primary_key=True)
    password = db.Column(
        db.String(120), nullable=False)
    shipping_address = db.Column(
        db.String(240), nullable=False)
    # postal code is usually 7 chars, 6 letter and 1 space
    postal_code = db.Column(
        db.String(12), nullable=False)
    balance = db.Column(
        db.Float(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Product(db.Model):
    # set id to primary_key and Integer and it would
    # increment automatically
    product_id = db.Column(
        db.Integer(), unique=True, nullable=False,
        primary_key=True)
    title = db.Column(
        db.String(80), nullable=False)
    description = db.Column(
        db.String(2000), nullable=False)
    price = db.Column(
        db.Float(), nullable=False)
    last_modified_date=db.Column(
        db.String(20), nullable=False)
    owner_email=db.Column(
        db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.title


class Review(db.Model):
    # set id to primary_key and Integer and it would
    # increment automatically
    review_id = db.Column(
        db.Integer(), unique=True, nullable=False,
        primary_key=True)
    user_email = db.Column(
        db.String(120), unique=True, nullable=False)
    score = db.Column(
        db.String(80), nullable=False)
    review = db.Column(
        db.String(2000), nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.score


class Transcation(db.Model):
    # set id to primary_key and Integer and it would
    # increment automatically
    transaction_id = db.Column(
        db.Integer(),unique=True, nullable=False,
        primary_key=True)
    user_email = db.Column(
        db.String(120), nullable=False)
    product_id = db.Column(
        db.Integer(), nullable=False)
    price = db.Column(
        db.Float(), nullable=False)
    date = db.Column(
        db.String(20), nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.transaction_id


# create all tables
db.create_all()



def register(name, email, password):
    '''
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    '''
    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False

    # create a new user
    user = User(username=name, email=email, password=password)
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()

    return True


def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]
