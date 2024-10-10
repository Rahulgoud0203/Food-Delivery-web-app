
from Food_Delivery_App import db


class Restaurents(db.Model):
    __tablename__ = 'restaurents'  # This defines the table name in the database.
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    address = db.Column(db.String(30), unique=False, nullable=False)
    img = db.Column(db.String(64), unique=True)
    
    # Relationship to the Menu model
    menuitems = db.relationship('Menu', backref='restaurent', lazy=True)
    
    def __repr__(self):
        return f"id: {self.id}, restaurentname: {self.name}, address: {self.address}"


class Menu(db.Model):
    __tablename__ = 'menu'  # Define the table name explicitly.
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String(64), unique=True, nullable=False)
    des = db.Column(db.String(30), nullable=False)
    
    # Foreign key linking to Restaurents table
    rest_id = db.Column(db.Integer, db.ForeignKey('restaurents.id'), nullable=False)
    
    def __repr__(self):
        return f"name: {self.name}, price: {self.price}, desc: {self.des}"





class Profile(db.Model):
    id=db.Column(db.Integer,primary_key=True)

    first_name=db.Column(db.String(20),unique=False,nullable=False)
    last_name=db.Column(db.String(20),unique=False,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    img = db.Column(db.String(64),unique=True)
    
    def __repr__(self):
        return f"Name  : {self.first_name}bAge:{self.age}"
    
class ProductItem(db.Model):
     __tablename__='products'
     id = db.Column(db.Integer,primary_key=True)
     name = db.Column(db.String(64),unique=True)
     descr = db.Column(db.Text,unique=True,nullable=True)
     price = db.Column(db.Float,nullable=False)
     img = db.Column(db.String(64),unique=True)
     cartitems = db.relationship('CartItem', backref='product')
     def _repr_(self):
         return '<ProductName %r>' % self.name

class CartItem(db.Model):
    __tablename__='cartitems'
    id = db.Column(db.Integer,primary_key=True)
    # adding the foreign key
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity=db.Column(db.Integer,nullable=False,default=1)
    
