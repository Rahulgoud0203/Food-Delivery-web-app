from datetime import datetime
from Food_Delivery_App import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Restaurents(db.Model):
    __tablename__ = 'restaurents'  # This defines the table name in the database.
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    address = db.Column(db.String(30), unique=False, nullable=False)
    img = db.Column(db.String(64), unique=True)
    
    # Relationship to the Menu model
    menuitems = db.relationship('MenuItems', backref='restaurent', lazy=True)
    
    def __repr__(self):
        return f"id: {self.id}, restaurentname: {self.name}, address: {self.address}"

class Profile(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)

    first_name=db.Column(db.String(20),unique=False,nullable=False)
    last_name=db.Column(db.String(20),unique=False,nullable=False)
    email=db.Column(db.String(30),unique=True,nullable=False)
    password=db.Column(db.String(20),unique=True,nullable=False)
    date_of_joined=db.Column(db.DateTime, default=datetime.utcnow)
    phone_no=db.Column(db.Integer,nullable=False)
    img = db.Column(db.String(64),unique=False)

    def set_password(self, password):
        """Hash the password and store it."""
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        """Check if the provided password matches the stored hash."""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Name  : {self.first_name}bAge:{self.age}"
    
class MenuItems(db.Model):
     __tablename__='menus'
     id = db.Column(db.Integer,primary_key=True)
     name = db.Column(db.String(64),unique=True)
     descr = db.Column(db.Text,unique=True,nullable=True)
     price = db.Column(db.Float,nullable=False)
     img = db.Column(db.String(64),unique=True)
     rest_id = db.Column(db.Integer, db.ForeignKey('restaurents.id'), nullable=False)
     cartitems = db.relationship('CartItem', backref='menu')
     
     def _repr_(self):
         return '<ProductName %r>' % self.name

class CartItem(db.Model):
    __tablename__='cartitems'
    id = db.Column(db.Integer,primary_key=True)
    # adding the foreign key
    product_id = db.Column(db.Integer, db.ForeignKey('menus.id'))
    quantity=db.Column(db.Integer,nullable=False,default=1)
    
