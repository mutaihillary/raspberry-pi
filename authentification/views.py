from flask import render_template, request, redirect, flash,url_for
from run import app

from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        form.name.data = ''
    return render_template('auth/login.html', form=form, login=login)


def registration():
    return render_template('auth/registration.html')

