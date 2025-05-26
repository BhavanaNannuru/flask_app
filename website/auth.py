from flask import Blueprint, render_template, request, flash

# Define the blue print of our application, routes. We cna have them done in multiple files using blue print.

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email)<4:
            flash('Email is too short!', category='error')
        elif len(firstname)<2:
            flash('First Name is too short!', category='error')

        elif password1!=password2:
            flash('Passwords dont match!', category='error')

        elif len(password1)<7:
            flash('Password is too short! Min 7', category='error')

        else:
            # Add user to database
            flash('Account created!', category='success')


    return render_template('signup.html')