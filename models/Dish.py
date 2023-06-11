from db import db

class Item(db.Model):
    __tablename__= 'item'
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), primary_key=True)
    amount = db.Column(db.Integer, nullable=False)

class Dish(db.Model):
    __tablename__= 'dish'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    is_gluten_free = db.Column(db.Boolean, nullable=False, default = False)
    is_vegetarian = db.Column(db.Boolean, nullable=False, default = False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    items = db.relationship('Item', backref='dish')