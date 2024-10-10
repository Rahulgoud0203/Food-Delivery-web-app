from flask import Blueprint,render_template,redirect,url_for
from Food_Delivery_App import db
from Food_Delivery_App.models import Restaurents

rest_bp=Blueprint('rest',__name__,template_folder='template/')

@rest_bp.route('/')
def index():

    rest=Restaurents(name="gita",address="gitabhavan ,karimnagar")
    db.session.add(rest)
    db.session.commit()
    return render_template("base.html")
