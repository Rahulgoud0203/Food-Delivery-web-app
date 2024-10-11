from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from Food_Delivery_App.models import Profile,db
from . import app
import os
from werkzeug.utils import secure_filename

auth = Blueprint('auth', __name__,template_folder='templates',static_folder='static')

UPLOAD_FOLDER = os.path.join('static', 'uploads')  # Path to the uploads directory
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Initialize Flask-Login's login manager
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


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
            return redirect(url_for('customers.index',))  # Redirect to a main page
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')
    
    return render_template('login.html')  # Render the login template

@auth.route('/logout'  ,methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    current_user=False
    print(current_user)
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))  # Redirect to login page

#####################################REGISTER##############################################################

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        password_confirm = request.form.get('passwordConfirm')
        phone_number = request.form.get('phoneNumber')
        avatar = request.files['avatar']
        
        if avatar:
            filename = secure_filename(avatar.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            avatar.save(file_path)
            
        else:
            file_path=None

        # Perform validations, save user data, etc.
        if not name or not email or not password or password != password_confirm:
            flash('Please fill in all required fields and make sure passwords match!', 'error')
            return redirect(url_for('auth.register'))

        else:
            try:
                new_user = Profile(name=name,email=email,phone_no=phone_number,img=file_path)
                new_user.set_password(password)
                db.session.add(new_user)
                db.session.commit()
                flash('Registration successful!', 'success')
                return redirect(url_for('auth.login'))
            except Exception as e:
                db.session.rollback()
                print(f"Error occurred: {e}")
                flash(f'Error: {str(e)}', 'danger')
        

    return render_template('register.html')
