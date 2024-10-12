from flask import Blueprint,render_template,redirect,url_for
from Food_Delivery_App import db
from Food_Delivery_App.models import Restaurants,MenuItems

rest_bp=Blueprint('rest',__name__,template_folder='template/')

@rest_bp.route('/')
def index():

    rest=Restaurants(name="gita",address="gitabhavan opposite sv ,karimnagar")
    db.session.add(rest)
    db.session.commit()
    rest1=Restaurants(name="swetha",address="gitabhavan ,karimnagar")
    db.session.add(rest1)
    db.session.commit()
    rest2=Restaurants(name="lucky",address="choke,busstop ,karimnagar")
    db.session.add(rest2)
    db.session.commit()
    return render_template("base.html")
@rest_bp.route('/add_menu')
def add_menu():
        existing_menu = MenuItems.query.filter_by(name='paratha').first()
        
        if existing_menu:
        
            return f"Menu item with name '{existing_menu.name}' already exists!"

        new_menu=[MenuItems(name="Biryani",descr="A food item made with seasoned rice, vegetables and sometimes meat.",price="234",rest_id="1")
        ,MenuItems(name="paratha",descr="Paratha is a flaky, layered, golden-brown Indian bread, which is typically consumed for breakfast. It consists of whole wheat flour that's baked in ghee ...",price="546",rest_id="1")]
    
        db.session.add_all(new_menu)
        try:
            db.session.commit()
            return f"Menu item {new_menu.name} added successfully!"
        except IntegrityError:
            db.session.rollback()  # Rollback in case of error
            return "Failed to add menu item due to a unique constraint violation."

        return render_template("base.html")