from flask import Blueprint,render_template,redirect,url_for
from flask_login import login_required,current_user
from Food_Delivery_App import db
from Food_Delivery_App.models import Restaurents


customers_bp=Blueprint('customers',__name__,static_folder='static',template_folder='templates/')

@customers_bp.route('/resturents')
@login_required
def index():
    
    rest=Restaurents.query.all()

    return render_template("index.html",restaurents=rest)

@customers_bp.route('/menu')
def menu():
    
    

    return render_template("index.html",rest=rest,current_user=current_user)
