from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
# Define the blue print of our application, routes. We cna have them done in multiple files using blue print.

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password DUDE!', category='error')
        else:
            flash("Its high time to create an account DUDE!",category='error')
    return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Theres Log In button up there for you!!', category='error')
        elif len(email)<4:
            flash('Lazy! Email is too short!', category='error')
        elif len(first_name)<2:
            flash('Cutie name i see! First Name is too short!', category='error')

        elif password1!=password2:
            flash('Uff! Just another day to crack ur nutshell! Passwords dont match!', category='error')

        elif len(password1)<7:
            flash('Alright, real work here! Password is too short! Min 7', category='error')

        else:
            new_user = User(email=email, first_name = first_name, password = generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)

            # Add user to database
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))



    return render_template('signup.html', user=current_user)