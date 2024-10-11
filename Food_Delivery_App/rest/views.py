from flask import Blueprint,render_template,redirect,url_for
from Food_Delivery_App import db
from Food_Delivery_App.models import Restaurents

rest_bp=Blueprint('rest',__name__,template_folder='template/')

@rest_bp.route('/')
def index():

    rest=Restaurents(name="gita",address="gitabhavan opposite sv ,karimnagar")
    db.session.add(rest)
    db.session.commit()
    rest1=Restaurents(name="swetha",address="gitabhavan ,karimnagar")
    db.session.add(rest1)
    db.session.commit()
    rest2=Restaurents(name="lucky",address="choke,busstop ,karimnagar")
    db.session.add(rest2)
    db.session.commit()
    return render_template("base.html")
