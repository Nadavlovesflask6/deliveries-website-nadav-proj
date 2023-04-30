from flask import Blueprint
from controllers.Customers import signup,login,adminlogin,userchange,dishmanagement,deliverymanagement,logout

customers_bp = Blueprint('customers',__name__)

customers_bp.add_url_rule('/signup',view_func=signup,methods=['GET','POST'])
customers_bp.add_url_rule('/login',view_func=login,methods=['GET','POST'])
customers_bp.add_url_rule('/admin-login',view_func=adminlogin,methods=['GET','POST'])
customers_bp.add_url_rule('/userchange',view_func=userchange,methods=['GET','POST'])
customers_bp.add_url_rule('/dishmanagement',view_func=dishmanagement)  
customers_bp.add_url_rule('/deliverymanagement',view_func=deliverymanagement, methods=['GET', 'POST'])
customers_bp.add_url_rule('/logout', view_func=logout)
