from flask import Blueprint
from controllers.Orders import order,orderhistory,cart,update_cart

orders_bp= Blueprint('orders',__name__)

orders_bp.add_url_rule('/order',view_func=order ,methods=['GET', 'POST'])
orders_bp.add_url_rule('/orderhistory',view_func=orderhistory)
orders_bp.add_url_rule('/cart',view_func=cart, methods=['GET', 'POST'])
orders_bp.add_url_rule('/update_cart',view_func=update_cart, methods=['POST'])
