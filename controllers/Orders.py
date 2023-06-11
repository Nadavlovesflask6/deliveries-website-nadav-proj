from flask import Blueprint,request,render_template,redirect,url_for,flash
from models.User import User
from models.Dish import Dish
from models.Delivery import Delivery
from models.Category import Category
from models.Cart import Cart
from models.Dish import Item
from db import db
from flask_login import current_user,login_required,login_user,logout_user

@login_required
def order():
    carts = Cart.query.all()
    my_cart_id = []
    for cart in carts:
        if cart.user_id == current_user.id:
            my_cart_id.append(cart.id)
    current_cart = Cart.query.get(my_cart_id[-1])
    if request.method == 'POST':
        new_delivery = Delivery(
            order_id=current_cart.id,
            address=request.form['address'],
            comment=request.form['comment']
        )
        db.session.add(new_delivery)
        db.session.commit()
        
        user_cart = Cart(user_id=current_user.id)
        db.session.add(user_cart)
        db.session.commit()
        return redirect(url_for("orders.orderhistory"))
    return render_template('order.html')

@login_required
def orderhistory():
    carts = Cart.query.all()
    my_carts = []
    for cart in carts:
        if cart.user_id == current_user.id:
            my_carts.append(cart)
    deliveries = Delivery.query.all()
    return render_template('orderhistory.html', deliveries=deliveries, my_carts=my_carts)

@login_required
def cart():
    user_cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not user_cart:
        user_cart = Cart(user_id=current_user.id)
        db.session.add(user_cart)
        db.session.commit()
    if request.method == 'POST':
        for dish_id in request.form.getlist('add_to_cart'):
            amount = int(request.form[dish_id])
            if amount > 0:
                item = Item.query.filter_by(dish_id=dish_id, cart_id=user_cart.id).first()
                if item:
                    item.amount += amount
                else:
                    item = Item(dish_id=dish_id, cart_id=user_cart.id, amount=amount)
                    db.session.add(item)
            else: 
                item = Item.query.filter_by(dish_id=dish_id, cart_id=user_cart.id).first()
                if item:
                    db.session.delete(item)
        for dish_id in request.form.getlist('update_cart'):
            amount = int(request.form[dish_id])
            item = Item.query.filter_by(dish_id=dish_id, cart_id=user_cart.id).first()
            if item and amount > 0:
                item.amount = amount
            elif item and amount <= 0: 
                db.session.delete(item)
        db.session.commit()
        flash('Cart updated.')
    items = Item.query.filter_by(cart_id=user_cart.id).all()
    final_sum = 0
    for item in items:
        dish = Dish.query.filter_by(id=item.dish_id).first()
        final_sum += float(dish.price) * float(item.amount)
    return render_template('cart.html', items=items, final_sum=final_sum)

def update_cart():
    dish_id = request.form['dish_id']
    amount = int(request.form['amount'])
    item = Item.query.filter_by(dish_id=dish_id).first()
    if item:
        if amount > 0:
            item.amount = amount
            db.session.commit()
            flash('Item updated successfully.')
        else:
            db.session.delete(item)
            db.session.commit()
            flash('Item removed from cart.')
    else:
        flash('Item not found.')
    return redirect(url_for('orders.cart'))