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
        db.DataTime(), nullable=False)
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
    user = User(username=name, email=email, password=password)
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


def create_product(Title, Description, Price, Last_modified_date, Owner_email):
    """
    Create a new product
        Parameters:
            Title (string):          product name
            Owner_email (string):    product owner email
            Description (string):    product description
            Price (float):           product price
            Last_modified_date (string): date of last modification of product
        Returns:
            true if registration succeeded otherwise False
    """

    # R4-1:The title of the product has to be alphanumeric-only,
    # and space allowed only if it is not as prefix and suffix.
    if Title[0] == ' ' or Title[-1] == ' ':
        return False
    else:
        tempTitle = Title.replace(" ", "")
        if not tempTitle.isalnum():
            return False
        # R4-2: The title of the product is no longer than 80 characters.
        elif len(Title) > 80:
            return False
    # R4-8: A user cannot create products that have the same title.
    validT = Product.query.filter_by(title=Title).all()
    if len(validT) != 1:
        return False

    # R4-4: Description has to be longer than the product's title.
    if len(Description) < len(Title):
        return False
    else:
        # R4-3: The description of the product can be arbitrary characters,
        # with a minimum length of 20 characters and a maximum of
        # 2000 characters.
        if len(Description) > 2000 or len(Description) < 20:
            return False

    # R4-5: Price has to be of range [10, 10000].
    if Price > 10000 or Price < 10:
        return False

    # R4-6: last_modified_date must be after 2021-01-02 and before 2025-01-02.
    while True:
        # Convert string time to the datetime type variable
        date_time_obj = datetime.strptime(Last_modified_date,
                                          '%Y-%m-%d').date()
        start = datetime.datetime.strptime("2021-01-02", '%Y-%m-%d')
        end = datetime.datetime.strptime("2025-01-02", '%Y-%m-%d')
        if Last_modified_date == '2022-02-29':
            break
        elif Last_modified_date == '2021-02-29' or \
                Last_modified_date == '2023-02-29' \
                or Last_modified_date == '2024-02-29':
            return False
        elif not (start <= date_time_obj <= end):
            return False

    # R4-7: owner_email cannot be empty(designed in model declaration).
    # The owner of the corresponding product must exist in the database.
    validO = Product.query.filter_by(owner_email=Owner_email).all()
    if len(validO) == 0:
        return False

    # create a new user
    product = Product(title=Title, description=Description,
                      price=Price, last_modified_date=Last_modified_date,
                      owner_email=Owner_email)
    # add it to the current database session
    db.session.add(product)
    # actually save the user object
    db.session.commit()
    return True


def updateProductTittle(ID, newTittle):
    '''
    Update product tittle
        Paraameters:
            ID(integer):     product ID
            tittle(String):  new product tittle
    '''
    # check if the tittle is not empty
    if (newTittle is not None) & (ID is not None):

        # update product tittle to the current database session
        db.session.query(Product).filter(Product.product_id == ID).\
            update({Product.tittle: newTittle}, synchronize_session = False)
        
        # update product update time to the current database session
        db.session.query(Product).filter(Product.product_id == ID).\
            update({Product.last_modified_date: datetime.now}, synchronize_session = False)
        
        # save the product object
        db.session.commit()
        return True
        
    else:
        return False

         
def updateProductDescription(ID, newDescription):
    '''
    Update product tittle
        Paraameters:
            ID(integer):     product ID
            newDescription(String):  new product description
    '''
    # check if the newDescription is not empty
    if (newDescription is not None) & (ID is not None):

        # update product description to the current database session
        db.session.query(Product).filter(Product.product_id == ID).\
            update({Product.description: newDescription}, synchronize_session = False)
        
        # update product update time to the current database session
        db.session.query(Product).filter(Product.product_id == ID).\
            update({Product.last_modified_date: datetime.now()}, synchronize_session = False)
        
        # save the product object
        db.session.commit()
        return True
        
    else:
        return False


def updateProductPrice(ID, newPrice):
    '''
    Update product tittle
        Paraameters:
            ID(integer):     product ID
            newPrice(Float):  new product price
    '''
    # get old price
    oldPrice = db.session.query(Product).filter(Product.price).one()
    
    # check whether new price is increase
    if (newPrice > oldPrice) & (ID is not None):

        # update product description to the current database session
        db.session.query(Product).filter(Product.product_id == ID).\
            update({Product.price: newPrice}, synchronize_session = False)
        
        # update product update time to the current database session
        db.session.query(Product).filter(Product.product_id == ID).\
            update({Product.last_modified_date: datetime.now()}, synchronize_session = False)
        
        # save the product object
        db.session.commit()
        return True
        
    else:
        return False