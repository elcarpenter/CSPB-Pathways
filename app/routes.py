from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user
from flask_login import login_required
from flask_login import logout_user
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, ReviewForm, PlanForm
from app.models import User, Review, SemesterSchedule

from basicGen import basicAlg
from reviews import *
from app.forms import LoginForm
from config import Config

import json
import datetime



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
@app.route('/about')
def about():
    user = {'username': 'Ryan'}
    return render_template('about.html')
'''

'''
@app.route('/plan', methods=['GET', 'POST'])
@app.route('/plan')
@login_required
def plan():
    # Default user id set to -1
    user_id = -1

    # Get the id of the current user that is logged in
    if current_user.is_authenticated:
        user = current_user.username
        user_object = User.query.filter_by(username=user).first()
        user_id = user_object.return_id()

    form = PlanForm()
    #user_plan = Review.query.all()
    # plan_list = []
    # for review in reviews_all: 
        # reviews_list.append((review.classname, review.hoursperweek, review.review, review.stars, review.timestamp, review.user_id))
    if form.validate_on_submit():
        ts = datetime.datetime.utcnow()
        # plan = SemesterSchedule(classname=form.classname.data, hoursperweek=form.hoursPerWeek.data, review=form.review.data, stars=form.stars.data, timestamp=ts, user_id=user_id)
        # db.session.add(plan)
        # db.session.commit()
        # redirect after posting review
        return redirect(url_for('plan'))
    else:
        # return render_template('plan.html', reviews=reviews_list, form=form)
        return render_template('plan.html', form=form)
'''

@app.route('/plan', methods=['GET', 'POST'])
@app.route('/plan')
def plan():

    # Default user id set to -1
    user_id = -1
    # form = PlanForm()
    # Get the id of the current user that is logged in
    if current_user.is_authenticated:
        user = current_user.username
        user_object = User.query.filter_by(username=user).first()
        user_id = user_object.return_id()

    if request.method == 'POST':
        selected_list = request.form.getlist('mycheckbox')
        selected_class = [class_dict[x] for x in selected_list]
        hours = int(request.form.getlist('hour_to_have')[0])
        elective = request.form.getlist('mycheckbox_elect')
        semester = int(request.form.getlist('mycheckbox_semester')[0])
        dontwant = request.form.getlist('mycheckbox_not')
        [class_to_take, tot_credit] = basicAlg(selected_class, hours, elective, semester, dontwant)
        # print(tot_credit)
        # '/user/<username>'
        # return redirect(url_for('plan'))
        return render_template('plan.html', classes=class_to_take, credit = tot_credit)
    else:
        classes = []
        return render_template('plan.html', classes=classes)

@app.route('/contact', methods=['GET', 'POST'])
@app.route('/contact')
def contact():
    user = {'username': 'Ryan'}
    return render_template('contact.html', user=user)


# @app.route decorators from Flask, the function becomes protected 
# and will not allow access to users that are not authenticated
@app.route('/updates')
@login_required
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
    # Default user id set to -1
    user_id = -1

    # Get the id of the current user that is logged in
    if current_user.is_authenticated:
        user = current_user.username
        user_object = User.query.filter_by(username=user).first()
        user_id = user_object.return_id()

    form = ReviewForm()
    reviews_all = Review.query.all()
    reviews_list = []
    for review in reviews_all: 
        reviews_list.append((review.classname, review.hoursperweek, review.review, review.stars, review.timestamp, review.user_id))
    if form.validate_on_submit():
        ts = datetime.datetime.utcnow()
        review = Review(classname=form.classname.data, hoursperweek=form.hoursPerWeek.data, review=form.review.data, stars=form.stars.data, timestamp=ts, user_id=user_id)
        db.session.add(review)
        db.session.commit()
        # redirect after posting review
        return redirect(url_for('reviews'))
    else:
        return render_template('reviews.html', reviews=reviews_list, form=form)

# Logs user out
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # redirect to home/index if user is logged in
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

