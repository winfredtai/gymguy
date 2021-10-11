import re
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
    last_modified_date = db.Column(
        db.String(20), nullable=False)
    owner_email = db.Column(
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
        db.Integer(), unique=True, nullable=False,
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


def check_username(username):
    '''
    Checks that username meets requirements
      Parameters:
        username (string):  user username
      Returns:
        True if username meets requirements otherwise False
    '''
    if not username:
        print("Username cannot be empty.")
        return False

    if username.startswith(" ", 0) or username.endswith(" "):
        print("Username cannot begin or end with a space.")
        return False

    if not username.replace(" ", "").isalnum():
        print("Username can only have letters and numbers.")
        return False

    if len(username) < 2 or len(username) > 20:
        print("Username must be between 2 and 20 characters.")
        return False

    return True


def check_shipping_address(shipping_address):
    '''
    Checks that shipping address meets requirements
      Parameters:
        shipping_address (string):  user shipping address
      Returns:
        True if address meets requirements otherwise False
    '''
    if not shipping_address:
        print("The shipping address must not be empty.")
        return False
    if not shipping_address.replace(" ", "").isalnum():
        print("The shipping address can only have letters and numbers.")
        return False
    return True


def check_postal_code(postal_code):
    '''
    Checks that postal code meets requirements
      Parameters:
        postal_code (string):   user postal code
      Returns:
        True if postal code meets requirements otherwise False
    '''
    if not re.fullmatch(r'\b[ABCEGHJ-NPRSTVXY]\d[ABCEGHJ-NPRSTV-Z]\s'
                        r'\d[ABCEGHJ-NPRSTV-Z]\d\b', postal_code):
        print("This is not a valid postal code.")
        return False
    return True


def register(name, email, password):
    '''
    Register a new user
      Parameters:
        name (string):      user name
        email (string):     user email
        password (string):  user password
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
    if check_email(email) is False:
        return None
    if check_password(password) is False:
        return None
    user = User.query.filter_by(email=email).first()
    if user.password == password:
        return user
    return None


def update_user(email, username, shipping_address, postal_code):
    '''
    Updates an existing user
      Parameters:
        email (string):             user email
        username (string):          user username
        shipping_address (string):  user shipping address
        postal_code (string):       user postal code
      Returns:
        True if user update succeeded otherwise False
    '''
    user = User.query.filter_by(email=email).first()
    if user is None:
        return False
    username_verification = check_username(username)
    shipping_address_verification = check_shipping_address(shipping_address)
    postal_code_verification = check_postal_code(postal_code)
    if username_verification and shipping_address_verification \
            and postal_code_verification:
        user.username = username
        user.shipping_address = shipping_address
        user.postal_code = postal_code
    db.session.commit()
    return True
