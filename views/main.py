"""Code Analyzer main view."""

from flask import Blueprint, render_template


main = Blueprint('main', __name__)


@main.route('/')
def home():
    """HomePage."""
    return render_template('home.html')
