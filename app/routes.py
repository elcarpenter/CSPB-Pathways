from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user
from flask_login import login_required
from flask_login import logout_user
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, ReviewForm
from app.models import User, Review

from basicGen import basicAlg
from reviews import *
from app.forms import LoginForm
from config import Config

import json

import datetime


class_dict = {
    '1': 1300,
    '2': 2824,
    '3': 2270,
    '4': 3104,
    '5': 2400,
    '6': 3308,
    '7': 3155,
    '8': 3702,
    '9': 3022,
    '10': 4122,
    '11': 4502,
    '12': 2820,
    '13': 3403
}


# @login_required
# @app.route decorators from Flask, the function becomes protected 
# and will not allow access to users that are not authenticated
@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template('index.html')

# User page that will select 
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html')
'''
@app.route('/test')
def dropdown():
    form = ReviewForm()
    colors = ['Red', 'Blue', 'Black', 'Orange']
    return render_template('test.html', colors=colors, form=form)
'''

@app.route('/about')
def about():
    user = {'username': 'Ryan'}
    return render_template('about.html')

@app.route('/plan', methods=['GET', 'POST'])
@app.route('/plan')
def plan():
    if request.method == 'POST':
        selected_list = request.form.getlist('mycheckbox')
        selected_class = [class_dict[x] for x in selected_list]
        to_take = basicAlg(selected_class)
        return render_template('plan.html', classes=to_take)
    else:
        classes = []
        return render_template('plan.html', classes=classes)

@app.route('/contact', methods=['GET', 'POST'])
@app.route('/contact')
def contact():
    user = {'username': 'Ryan'}
    return render_template('contact.html', user=user)

@app.route('/updates')
def updates():
    user = {'username': 'Ryan'}
    posts = [
        {
            'author': {'username': 'Ryan'},
            'body': 'The teacher gave us an A+ what a nice guy!'
        },
        {
            'author': {'username': 'Ryan'},
            'body': 'Set up for our first sprint'
        },
        {
            'author': {'username': 'Ryan'},
            'body': 'Everyone is talking about how cool this project is!'
        }
    ]
    return render_template('updates.html', user=user, posts=posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    #if current_user.is_authenticated:
        #return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        
    return render_template('register.html', form=form)

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    form = ReviewForm()
    reviews_all = Review.query.all()
    reviews_list = []
    for review in reviews_all: 
        reviews_list.append((review.classname, review.hoursperweek, review.review, review.stars, review.timestamp))
    if form.validate_on_submit():
    # if request.method == 'POST':
        # selected_list = request.form.getlist('mycheckbox')
        # reviews = review_printer(selected_list)
        ts = datetime.datetime.utcnow()
        review = Review(classname=form.classname.data, hoursperweek=form.hoursPerWeek.data, review=form.review.data, stars=form.stars.data, timestamp=ts)
        # v = classname=form.title.data
        # v1 = hoursperweek=form.hoursPerWeek.data
        # v2 = review=form.review.data
        # v3 = stars=form.stars.data
        # return str(str(v) + " " + str(v1) + " " + str(v2) + " " + str(v3))
        db.session.add(review)
        db.session.commit()
        return render_template('reviews.html', reviews=reviews_list, form=form)
    else:
        return render_template('reviews.html', reviews=reviews_list, form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # recirect to home/index if user i slogged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('You entered an invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

