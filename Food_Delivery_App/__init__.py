import os
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SECRET_KEY']='mykey'

basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlit')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

Migrate(app,db)


from Food_Delivery_App.customers.views import customers_bp
from Food_Delivery_App.rest.views import rest_bp
from Food_Delivery_App.auth import auth

app.register_blueprint(customers_bp,url_prefix='/')
app.register_blueprint(rest_bp,url_prefix='/rest')
app.register_blueprint(auth, url_prefix='/auth')



