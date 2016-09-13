from flask import render_template, request, redirect, flash,url_for
from run import app

from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html', login=login)


def registration():
    return render_template('auth/registration.html')