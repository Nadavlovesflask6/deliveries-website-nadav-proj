from db import db
from datetime import datetime as dt

class Delivery(db.Model):
    __tablename__= 'delivery'
    order_id = db.Column(db.Integer, db.ForeignKey('cart.id'), primary_key=True)
    is_delivered = db.Column(db.Boolean, nullable=False, default=False)
    address = db.Column(db.String(200), nullable=False)
    comment = db.Column(db.String(200))
    created = db.Column(db.DateTime, nullable=False, default=dt.now)