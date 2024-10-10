from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from Food_Delivery_App.models import Profile
from . import app
auth = Blueprint('auth', __name__,template_folder='templates')

# Initialize Flask-Login's login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return Profile.query.get(int(user_id))  # Adjust User model according to your needs

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = Profile.query.filter_by(email=email).first()  # Query the user based on the email
        print(user)
        if user and user.verify_password(password):  # Verify the password
            login_user(user)  # Log in the user
            flash('Login successful!', 'success')
            return redirect(url_for('customers.rest'))  # Redirect to a main page
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')
    
    return render_template('login.html')  # Render the login template

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))  # Redirect to login page



@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name=request.form['name']
        cpassword=request.form['passwordConfirm']
        phonenm=request.form['phoneNumber']
        img=request.form['avatar']




        new_user = Profile(email=email,name=name,phone_no=phonenm,img=img)
        if cpassword==password:
            new_user.set_password(password)  # Hash the password before saving
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')
