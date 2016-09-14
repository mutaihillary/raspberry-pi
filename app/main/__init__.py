from flask import Blueprint, render_template
from . import views, errors
main = Blueprint('main', __name__)


def registration():
    return render_template('auth/registration.html')
