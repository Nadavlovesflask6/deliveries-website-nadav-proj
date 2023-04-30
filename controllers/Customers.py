from flask import Blueprint,request,render_template,redirect,url_for,flash
from models.User import User
from models.Dish import Dish
from models.Delivery import Delivery
from models.Category import Category
from db import db
from flask_login import current_user,login_required,login_user,logout_user

def signup():
    if request.method == 'POST':  
        new_account = User(
            username=request.form['username'],
            password=request.form['password'],
            first_name=request.form['first_name'],
            last_name=request.form['last_name'],
            email = request.form['email']
        )
        db.session.add(new_account)
        db.session.commit()
        return render_template('login.html', new_account=new_account)
    else:
        return render_template('signup.html')
    
def login():
    if current_user.is_authenticated:
        return redirect(url_for('foods.categories'))
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user != None:
            if request.form['password'] == user.password:
                login_user(user)
                flash('You have been successfully logged in.','success')
                return redirect(url_for('foods.categories'))
            else:
                flash('The username and password you logged with are incorrect.','error')
        else:
            flash('No user found with this username.','error')

    return render_template('login.html')

def adminlogin():
    if current_user.is_authenticated:
        return redirect(url_for('customers.dishmanagement'))
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user != None and user.is_staff:
            if request.form['password'] == user.password:
                login_user(user)
                flash('You have been successfully logged in.','success')
                return redirect(url_for('customers.dishmanagement'))
            else:
                flash('Invalid password.', 'error')
        else:
            flash('You are not authorized to access the admin panel.', 'error')
    return render_template('adminlogin.html')

@login_required
def userchange():
    if request.method == 'POST':
        user = User.query.get(current_user.id)
        user.username = request.form['username']
        user.password = request.form['password']
        db.session.commit()
        flash('Your details have been updated!')
        return redirect(url_for('customers.userchange'))
    return render_template('userchange.html', user=current_user)

@login_required
def dishmanagement():
    if not current_user.is_staff:
        flash('This page is for admins only.')
        return redirect(url_for('customers.login'))
    categories = Category.query.all()
    dishes = Dish.query.all()
    return render_template('dishmanagement.html', categories=categories, dishes=dishes)

@login_required
def deliverymanagement():
    if not current_user.is_staff:
        flash('This page is for admins only.')
        return redirect(url_for('customers.login'))
    deliveries = Delivery.query.all()
    if request.method == 'POST':
        delivery_id = request.form['delivery']
        current_delivery = Delivery.query.filter_by(order_id=delivery_id).first()
        current_delivery.is_delivered = True
        db.session.commit()
    return render_template('deliverymanagement.html', deliveries=deliveries)

def logout():
    logout_user()
    return redirect(url_for('customers.login'))