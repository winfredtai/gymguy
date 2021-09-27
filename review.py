from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime  # Import datatime package for later use


# __name__ is just a convenient way to get the import name of the
# place the app is defined. Flask uses the import
# name to know where to look up resources, templates, static files,
# instance folder, etc.
app = Flask(__name__)
# Configure the database URI that should be used for the connection
# to sqlite:///db.sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# Connect flask to a database.
db = SQLAlchemy(app)


# Declare the review model based on db form.
class Review(db.Model):
    # First attribute of review model is going to be user name and set
    # it with true primary key.
    # Since user name can be used to identify different reviews.
    username = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    # Second attribute of review model is going to be feed back rating.
    # It's a float number with 2 decimal places, users rate their
    # experience in float number range(0,10)
    feedback_rating = db.Column(db.Float(length=2, precision=2))
    # Third attribute of review model is going to be item condition.
    # It's a short string phrase containing three possible choices:
    # good, neutral, bad.
    item_condition = db.Column(db.String(120), unique=True, nullable=False)
    # Fourth attribute of review model is going to be seller name.
    # It's settled with true primary key since it can also identifies
    # the review different reviews.
    seller_name = db.Column(db.String(120), primary_key=True, unique=True, nullable=False)
    # Fifth attribute of review model is going to be comment content.
    # It could be sentence or paragraphs.
    comment = db.Column(db.String(500), unique=True, nullable=False)
    # Sixth attribute of review model is going to be the date user leaving review.
    # It require the data time from the imported datatime package.
    comment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.username
