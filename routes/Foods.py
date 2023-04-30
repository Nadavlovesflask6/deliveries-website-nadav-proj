from flask import Blueprint
from controllers.Foods import dishes,add_dish,edit_dish,delete_dish,categories,show_categories,add_category,edit_category,delete_category

foods_bp = Blueprint('foods',__name__)

foods_bp.add_url_rule('/dishes/<int:id>',view_func=dishes)
foods_bp.add_url_rule('/dish/add',view_func=add_dish, methods=['GET', 'POST'])
foods_bp.add_url_rule('/dish/edit/<int:id>',view_func=edit_dish, methods=['GET', 'POST'])
foods_bp.add_url_rule('/dish/<int:id>/delete',view_func=delete_dish)
foods_bp.add_url_rule('/categories',view_func=categories)
foods_bp.add_url_rule('/categories/<int:id>',view_func=show_categories)
foods_bp.add_url_rule('/category/add',view_func=add_category, methods=['GET', 'POST'])
foods_bp.add_url_rule('/category/edit/<int:id>',view_func=edit_category, methods=['GET', 'POST'])
foods_bp.add_url_rule('/category/<int:id>/delete',view_func=delete_category)