"""This Module Handles the User Related Routes"""

import flask
from werkzeug.security import check_password_hash
from flask import render_template, url_for, Blueprint, redirect, flash
from blog.users.forms import LoginForm
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user

users = Blueprint('users', __name__)


@users.route("/login", methods=['GET', 'POST'])
def login():
    """This function handles the user login"""
    post = Post.query.all()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('login unsuccessful! please recheck your details!', 'danger')
    return render_template('login.html', form=form, post=post, title='Login', directive='noindex')


@users.route('/logout')
def logout():
    """Logout Route"""
    logout_user()       
    return redirect(url_for('main.home'))