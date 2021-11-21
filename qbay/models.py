import re
from qbay import app
from flask_sqlalchemy import SQLAlchemy
import datetime

'''
This file defines data models and related business logics
'''

db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(
        db.String(80), nullable=False)
    # R1-1 email and password cannot be empty
    # R1-2 user is uniquely identified by his/her email address
    email = db.Column(
        db.String(120), unique=True, nullable=False,
        primary_key=True)
    password = db.Column(
        db.String(120), nullable=False)
    # R1-8 Shipping address is empty at the time of
    # registration.
    shipping_address = db.Column(
        db.String(240), default=None, nullable=True)
    # postal code is usually 7 chars, 6 letter and 1 space
    # R1-9
    postal_code = db.Column(
        db.String(12), default=None, nullable=True)
    # R1-10 balance is initialized as 100
    balance = db.Column(
        db.Float(), default=100.0, nullable=False)

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
        db.DateTime, nullable=False)
    owner_email = db.Column(
        db.String(120), nullable=False)

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


class Transaction(db.Model):
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

    if len(username) <= 2 or len(username) >= 20:
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


def check_password(password):
    '''
    Checks that password meets requirements
      Parameters:
        password(string):   user password
      Returns:
        True if password meets requirements otherwise False
    '''
    upper = 0
    lower = 0
    special = 0
    if len(password) >= 6:
        for i in password:
            if i.isupper():
                upper += 1
            if i.islower():
                lower += 1
            if i in "~\\!@#$%^&*()_+-*/<>,.[]":
                special += 1
        if (upper > 0) and (lower > 0) and (special > 0):
            return True
    return False


def check_email(email):
    '''
    Checks that email meets requirements
      Parameters:
        email(string): user email
      Returns:
        True if email meets requirements otherwise False
    '''
    # regular expression of RFC 5322, have tested the validation locally
    email_pattern = '''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?
    ^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[
    \x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[
    a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][
    0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[
    \x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[
    \x01-\x09\x0b\x0c\x0e-\x7f])+)\\])'''
    pat = re.compile(email_pattern)
    if re.fullmatch(pat, email):
        return True
    else:
        return False


def check_title(title):
    '''
    Checks that product title meets requirements
      Parameters:
        title(string): product title
      Returns:
        True if product title meets requirements otherwise False
    '''
    # R4-1:The title of the product has to be alphanumeric-only,
    # and space allowed only if it is not as prefix and suffix.
    validT = Product.query.filter_by(title=title).all()
    if len(validT) > 0:
        return False
    elif title[0] == ' ' or title[-1] == ' ':
        return False
    else:
        tempTitle = title.replace(" ", "")
        if not tempTitle.isalnum():
            return False
        # R4-2: The title of the product is no longer than 80 characters.
        elif len(title) > 80:
            return False
    return True


def check_description(description, title):
    '''
    Checks that product description meets requirements
      Parameters:
        description(string): product description
        title(string): product title
      Returns:
        True if product description meets requirements otherwise False
    '''
    # R4-4: Description has to be longer than the product's title.
    if len(description) <= len(title):
        return False
    # R4-3: The description of the product can be arbitrary characters,
    # with a minimum length of 20 characters and a maximum of
    # 2000 characters.
    elif len(description) > 2000 or len(description) < 20:
        return False
    return True


def check_price(price):
    '''
    Checks that product price meets requirements
      Parameters:
        price(float): product price
      Returns:
        True if product price meets requirements otherwise False
    '''
    if type(price) != int and type(price) != float:
        print("invalid price")
        return False
    # R4-5: Price has to be of range [10, 10000].
    if price > 10000 or price < 10:
        return False
    return True


def check_date(date):
    '''
    Checks that product date meets requirements
      Parameters:
        date(datetime object): last modified date
      Returns:
        True if product price meets requirements otherwise False
    '''
    # Convert string time to the datetime type variable
    start = datetime.datetime.strptime("2021-01-02", '%Y-%m-%d')
    end = datetime.datetime.strptime("2025-01-02", '%Y-%m-%d')
    if start <= date <= end:
        return True
    else:
        return False


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
    # R1-1
    if not email or not password:
        return False
    # R1-3 email has to follow addr-spec
    if not check_email(email):
        return False
    # R1-4 password has to meet the required complexity
    if not check_password(password):
        return False
    # R1-5 & R1-6 User name specification
    if not check_username(name):
        return False
    # R1-7 check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False
    # create a new user
    user = User(username=name, email=email, password=password,
                shipping_address=None, postal_code=None, balance=100.0)
    # R1-2 specified in User()
    # R1-8
    if user.shipping_address is not None:
        return False
    # R1-9
    if user.postal_code is not None:
        return False
    # R1-10
    if user.balance != 100.0:
        return False
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
    if not user:
        return None  # did not find the user
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
    else:
        return False


def create_product(Title, Description, Price, Owner_email):
    """
    Create a new product
        Parameters:
            Title (string):          product name
            Owner_email (string):    product owner email
            Description (string):    product description
            Price (float):           product price
        Returns:
            true if registration succeeded otherwise False
    """

    # R4-1:The title of the product has to be alphanumeric-only,
    # and space allowed only if it is not as prefix and suffix.
    # R4-2: The title of the product is no longer than 80 characters.
    # R4-8: A user cannot create products that have the same title.
    if not check_title(Title):
        return False
    # R4-3: The description of the product can be arbitrary characters,
    # with a minimum length of 20 characters and a maximum of 2000 characters.
    # R4-4: Description has to be longer than the product's title.
    if not check_description(Description, Title):
        return False

    # R4-5: Price has to be of range [10, 10000].
    if not check_price(Price):
        return False
    # R4-6: last_modified_date must be after 2021-01-02 and before 2025-01-02.
    dayTime = datetime.datetime.now()
    if not check_date(dayTime):
        return False
    # R4-7: owner_email cannot be empty(designed in model declaration).
    # The owner of the corresponding product must exist in the database.
    validO = User.query.filter_by(email=Owner_email).all()
    if len(validO) == 0:
        return False

    # create a new user
    product = Product(title=Title, description=Description,
                      last_modified_date=dayTime,
                      price=Price, owner_email=Owner_email)
    # add it to the current database session
    db.session.add(product)
    # actually save the user object
    db.session.commit()
    return True


def update_product(old_title, newDescription=None, newPrice=None,
                   newTitle=None):
    product = Product.query.filter_by(title=old_title).first()
    if product is None:
        return False
    if newTitle is not None:
        if newTitle != old_title:
            if not check_title(newTitle):
                return False
    if newDescription is not None:
        if not check_description(newDescription, newTitle):
            return False
    if newPrice is not None:
        if not check_price(newPrice):
            return False
        if product.price > newPrice:
            return False
    old_modified_date = product.last_modified_date
    date = datetime.datetime.now()
    if not check_date(date):
        return False
    if newTitle is not None:
        product.title = newTitle
    if newDescription is not None:
        product.description = newDescription
    if newPrice is not None:
        product.price = newPrice
    product.last_modified_date = date
    db.session.commit()
    if product.last_modified_date is not old_modified_date:
        print("last modified changed")
    return True
