from flask import Blueprint,render_template,redirect,url_for
from Food_Delivery_App import db
from Food_Delivery_App.models import Restaurents

customers_bp=Blueprint('customer',__name__,static_folder='static',template_folder='templates/')

@customers_bp.route('/')
def index():
    rest=Restaurents.query.all()

    return render_template("index.html",rest=rest)

@customers_bp.route('/menu')
def menu():
    
    

    return render_template("index.html",rest=rest)
