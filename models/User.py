from db import db
from flask_login import UserMixin
class User(db.Model,UserMixin):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(40), nullable=False)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    is_staff = db.Column(db.Boolean,default=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    carts = db.relationship('Cart', backref='user')