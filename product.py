from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    condition = db.Column(db.String(60), nullable=False)  # deal with this later! should be selection not string
    seller = db.Column(db.String(50), unique=True, nullable=False)
    modelNum = db.Column(db.Integer)
    color = db.Column(db.String(60), nullable=False)  # deal with this later! maybe should be selection not string
    category = db.Column(db.String(60), nullable=False)  # deal with this later! should be selection not string
    description = db.Column(db.String(1500), nullable=False)
