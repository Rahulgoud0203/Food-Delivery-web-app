from datetime import datetime
from Food_Delivery_App import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Restaurants(db.Model):
    __tablename__ = 'restaurents'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    address = db.Column(db.String(30), unique=False, nullable=False)
    img = db.Column(db.String(64), unique=True)

    # Define the relationship
    menu_items = db.relationship('MenuItems', back_populates='restaurant')

    def __repr__(self):
        return f"id: {self.id}, restaurentname: {self.name}, address: {self.address}"

class Profile(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), unique=True, nullable=False)  # Increase hash length
    date_of_joined = db.Column(db.DateTime, default=datetime.utcnow)
    phone_no = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String(64), unique=False)

    def __init__(self, email, name, phone_no, img=None):
        self.email = email
        self.name = name
        self.phone_no = phone_no
        self.img = img

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Name: {self.name}, email: {self.email}"

class MenuItems(db.Model):
    __tablename__ = 'menu_items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    descr = db.Column(db.Text, unique=True, nullable=True)
    price = db.Column(db.Float, nullable=False)
    img = db.Column(db.String(64), unique=True)
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurents.id'), nullable=False)

    restaurant = db.relationship('Restaurants', back_populates='menu_items')
    cart_items = db.relationship('CartItem', back_populates='menu_item')

    def __repr__(self):
        return '<ProductName %r>' % self.name

class CartItem(db.Model):
    __tablename__ = 'cartitems'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('menu_items.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    
    menu_item = db.relationship('MenuItems', back_populates='cart_items')
