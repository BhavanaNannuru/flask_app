# Store the standards routes of our page other than auth

from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Define the blue print of our application, routes. We cna have them done in multiple files using blue print.
views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html")