from flask import Blueprint,request,render_template,redirect,url_for,flash
from models.User import User
from models.Dish import Dish
from models.Delivery import Delivery
from models.Category import Category
from db import db
from flask_login import current_user,login_required,login_user,logout_user

@login_required
def dishes(id):
    dish = Dish.query.get(id)
    return render_template('dishes.html', dish=dish)

@login_required
def add_dish():
    if not current_user.is_staff:
        flash('This page is for admins only.')
        return redirect(url_for('customers.login'))
    categories = Category.query.all()
    if request.method == 'POST':
        new_dish = Dish(
            name=request.form['dish_name'],
            price=request.form['dish_price'],
            description=request.form['dish_description'],
            image=request.form['dish_imageurl'],
            is_gluten_free=bool(request.form.get('dish_is_gluten_free')),
            is_vegetarian=bool(request.form.get('dish_is_vegetarian')),
            category_id=request.form['dish_category']
        )
        db.session.add(new_dish)
        db.session.commit()
        flash('New dish added successfully!')
        return redirect(url_for('customers.dishmanagement'))
    return render_template('add_dish.html', categories=categories)

@login_required
def edit_dish(id):
    if not current_user.is_staff:
        flash('This page is for admins only.')
        return redirect(url_for('customers.login'))
    dish = Dish.query.get(id)
    categories = Category.query.all()
    if request.method == 'POST':
        dish.name = request.form['dish_name']
        dish.price = request.form['dish_price']
        dish.description = request.form['dish_description']
        dish.image = request.form['dish_imageurl']
        dish.is_gluten_free = bool(request.form.get('dish_is_gluten_free'))
        dish.is_vegetarian = bool(request.form.get('dish_is_vegetarian'))
        dish.category_id=request.form['dish_category']
        db.session.commit()
        flash('Dish updated successfully!')
        return redirect(url_for('customers.dishmanagement'))
    return render_template('edit_dish.html', dish=dish, categories=categories)

@login_required
def delete_dish(id):
    dish = Dish.query.get(id)
    db.session.delete(dish)
    db.session.commit()
    flash(f"{dish.name} has been deleted.")
    return redirect(url_for('customers.dishmanagement'))

@login_required
def categories():
    categories = Category.query.all()
    return render_template('categories.html',categories=categories)

@login_required
def show_categories(id):
    category = Category.query.get(id)
    dishes = Dish.query.all()
    dish_category = []
    for dish in dishes:
        if dish.category_id == category.id:
            dish_category.append(dish)
    return render_template('show_categories.html', category=category, dish_category=dish_category, dishes=dishes)

@login_required
def add_category():
    if not current_user.is_staff:
        flash('This page is for admins only.')
        return redirect(url_for('customers.login'))
    if request.method == 'POST':
        new_category = Category(
            name=request.form['category_name'],
            image=request.form['category_imageurl']
        )
        db.session.add(new_category)
        db.session.commit()
        flash('New category added successfully!')
        return redirect(url_for('customers.dishmanagement'))
    return render_template('add_category.html')

@login_required
def edit_category(id):
    if not current_user.is_staff:
        flash('This page is for admins only.')
        return redirect(url_for('customers.login'))
    category = Category.query.get(id)
    if request.method == 'POST':
        category.name = request.form['category_name']
        category.image = request.form['category_imageurl']
        db.session.commit()
        flash('Category updated successfully!')
        return redirect(url_for('customers.dishmanagement'))
    return render_template('edit_category.html', category=category)

@login_required
def delete_category(id):
    category = Category.query.get(id)
    db.session.delete(category)
    db.session.commit()
    flash(f"{category.name} has been deleted.")
    return redirect(url_for('customers.dishmanagement'))