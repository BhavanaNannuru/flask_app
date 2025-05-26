from flask import Blueprint

# Define the blue print of our application, routes. We cna have them done in multiple files using blue print.

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign-up</p>"