# Store the standards routes of our page other than auth

from flask import Blueprint

# Define the blue print of our application, routes. We cna have them done in multiple files using blue print.
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Hello, World!</h1>"