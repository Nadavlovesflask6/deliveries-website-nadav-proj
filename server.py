from flask import Flask,render_template,request,redirect,url_for
from db import db
from auth import login_manager
from routes.Customers import customers_bp
from routes.Foods import foods_bp
from routes.Orders import orders_bp
from config import DBUSER, DBPASS, DBHOST

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdaw4q4aw4ase213'
# app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///Restaurant.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}/postgres'
# app.config['SECRET_KEY'] = "<random password>"
db.init_app(app)
login_manager.init_app(app)

    
@app.route('/')
def main():
    return render_template('main.html')

with app.app_context():
    db.create_all()
    
app.register_blueprint(customers_bp)
app.register_blueprint(foods_bp)
app.register_blueprint(orders_bp)

app.run(debug=True, host="0.0.0.0")



#https://github.com/Nadavlovesflask6/Deliverysiteproj2.git