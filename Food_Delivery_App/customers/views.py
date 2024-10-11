from flask import Blueprint,render_template,redirect,url_for,flash
from flask_login import login_required,current_user
from Food_Delivery_App import db
from Food_Delivery_App.models import CartItem, MenuItems, Profile, Restaurents
from sqlalchemy import func

customers_bp=Blueprint('customers',__name__,static_folder='static',template_folder='templates/')
@customers_bp.route('/profile')
def profile():
    if current_user.is_authenticated:
        user_id = current_user.id
        profile=Profile.query.filter_by(id=user_id).first()
        print(profile.name)
        print(profile.date_of_joined)
    
        return render_template("profile.html",profile=profile)
    else:
        flash('You need to log in to access profile page.')
        return redirect(url_for('auth.login'))


@customers_bp.route('/resturents')
def rest():

    total_cart_quantity = db.session.query(func.sum(CartItem.quantity)).scalar() or 0
    resto=Restaurents.query.all()
    resto_count= db.session.query(Restaurents).count()

    return render_template("resto.html",restaurents=resto,resto_count=resto_count,total_cart=total_cart_quantity)

@customers_bp.route('/menu/<int:rest_id>')
def menu(rest_id):
    
   menuitems= MenuItems.query.all(rest_id=rest_id)
   return render_template("index.html",menu=menuitems)

@customers_bp.route('/view_cart')
def view_cart():
    cart=CartItem.query.all()
    return render_template("cart.html",cart=cart)





@customers_bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = MenuItems.query.get_or_404(product_id)
    
    # Check if the product is already in the cart
    cart_item = CartItem.query.filter_by(product_id=product_id).first()
    
    if cart_item:
        # If the product is already in the cart, increase the quantity
        cart_item.quantity += 1
    else:
        # Otherwise, add a new item to the cart with a default quantity of 1
        cart_item = CartItem(product_id=product.id, quantity=1)
        db.session.add(cart_item)
    
    db.session.commit()
    """return redirect(url_for('customers.menu'rest_id=))"""

@customers_bp.route('/update_cart/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    cart_item = CartItem.query.filter_by(product_id=product_id).first_or_404()
    
    # Get the new quantity from the form
    new_quantity = int(request.form.get('quantity', 1))
    
    if new_quantity > 0:
        cart_item.quantity = new_quantity
        db.session.commit()
    else:
        # If the quantity is less than 1, remove the item from the cart
        db.session.delete(cart_item)
        db.session.commit()

    return redirect(url_for('view_cart'))


@customers_bp.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    cart_item = CartItem.query.filter_by(product_id=product_id).first_or_404()
    
    # Remove the cart item from the database
    db.session.delete(cart_item)
    db.session.commit()

    return redirect(url_for('customers.view_cart'))