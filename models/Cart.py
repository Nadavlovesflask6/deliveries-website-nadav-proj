from db import db
class Cart(db.Model):
    __tablename__= 'cart'
    id = db.Column(db.Integer, primary_key=True )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_id = db.relationship('Delivery', backref='cart', uselist=False)