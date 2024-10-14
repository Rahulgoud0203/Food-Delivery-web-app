from flask import Blueprint,render_template,redirect,url_for,flash,request,jsonify
from flask_login import login_required,current_user
from Food_Delivery_App import db
from Food_Delivery_App.models import CartItem, MenuItems, Profile,Restaurants
from sqlalchemy import func

customers_bp=Blueprint('customers',__name__,static_folder='static',template_folder='templates')


@customers_bp.route('/menu/<int:rest_id>',methods=['GET', 'POST'])
@login_required
def menu(rest_id):
    items=MenuItems.query.filter_by(rest_id=rest_id)
    carts=CartItem.query.all()
    total_cart=0
    for cart in carts:
        total_cart+=cart.quantity
    
    return render_template('menus.html',items=items,total_cart=total_cart)

@customers_bp.route('/cart_button/<int:rest_id>/<int:menu_id>', methods=['POST','GET'])
def cart_button(rest_id,menu_id):
    print(menu_id)
    print("rest:",rest_id)
    add_to_cart(menu_id)
    return redirect(url_for('customers.menu', rest_id=rest_id)) 

@customers_bp.route('/profile')
def profile():
    carts=CartItem.query.all()
    total_cart=0
    for cart in carts:
        total_cart+=cart.quantity
    if current_user.is_authenticated:
        user_id = current_user.id
        profile=Profile.query.filter_by(id=user_id).first()
        print(profile.name)
        print(profile.date_of_joined)
    
        return render_template("profile.html",profile=profile, total_cart= total_cart)
    else:
        flash('You need to log in to access profile page.')
        return redirect(url_for('auth.login'))


@customers_bp.route('/resturents')
def rest():

    carts=CartItem.query.all()
    total_cart=0
    for cart in carts:
        total_cart+=cart.quantity
    resto=Restaurants.query.all()
    resto_count= db.session.query(Restaurants).count()

    return render_template("resto.html",restaurents=resto,resto_count=resto_count,total_cart=total_cart)




@customers_bp.route('/view_cart',methods=['POST','GET'])
@login_required
def view_cart():
    cart_items = CartItem.query.all()
    total_price=0
    menu_items_details = []
    total_cart=0
    for cart_item in cart_items:
        total_cart+=cart_item.quantity
        menu_item = MenuItems.query.get(cart_item.product_id) 
        rest=Restaurants.query.filter_by(id=menu_item.rest_id).first()
        if menu_item:
            total_price += menu_item.price *cart_item.quantity  # Check if the menu item exists
            menu_items_details.append({
                'name': menu_item.name,
                'description': menu_item.descr,
                'price': menu_item.price,
                'quantity': cart_item.quantity,
                'img': menu_item.img,  # Include image if needed
                'total_price': cart_item.quantity * menu_item.price ,
                'cart_id':cart_item.id,
                'resto_name':rest.name
            })

    # Render the cart template and pass the menu items' details
    return render_template("cart.html", carts=menu_items_details,total_price=total_price,total_cart=total_cart)




def add_to_cart(product_id):
    product = MenuItems.query.get_or_404(product_id)
    
    # Check if the product is already in the cart
    cart_item = CartItem.query.filter_by(product_id=product_id).first()
    print(f"Adding menu item with ID: {product_id}") 
    if cart_item:
        # If the product is already in the cart, increase the quantity
        cart_item.quantity += 1
    else:
        # Otherwise, add a new item to the cart with a default quantity of 1
        cart_item = CartItem(product_id=product.id, quantity=1)
        db.session.add(cart_item)
    
    db.session.commit()
    

@customers_bp.route('/update_cart/<int:item_id>', methods=['POST'])
@login_required
def update_cart(item_id):
    cart_item = CartItem.query.filter_by(product_id=item_id).first_or_404()
    action = request.form.get('action')
    if action == 'increase':
        cart_item.quantity += 1
        db.session.commit()

    elif action == 'decrease' and cart_item.quantity > 1:
       cart_item.quantity -= 1
       db.session.commit()
    elif action =='decrease'and cart_item.quantity==1:
        db.session.delete(cart_item)
        db.session.commit()

    return redirect(url_for('customers.view_cart'))


@customers_bp.route('/cart/delete/<int:item_id>', methods=['POST'])
@login_required
def delete_cart_item(item_id):
    # Query the cart item using the provided ID
    cart_item = CartItem.query.get(item_id)
    if request.method == 'POST':
        if cart_item:

            db.session.delete(cart_item)
            db.session.commit()
        return redirect(url_for('customers.view_cart'))
    return redirect(url_for('customers.view_cart'))