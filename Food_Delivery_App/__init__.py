import os
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SECRET_KEY']='mykey'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlit')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

Migrate(app,db)


from Food_Delivery_App.customers.views import customers_bp
from Food_Delivery_App.rest.views import rest_bp
from Food_Delivery_App.auth import auth

app.register_blueprint(customers_bp,url_prefix='/customers')
app.register_blueprint(rest_bp,url_prefix='/rest')
app.register_blueprint(auth, url_prefix='/auth')



