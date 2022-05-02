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
# from reviews import *
from cspbAlg import *
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
    '13': 3403,
    '14': 3202,
    '15': 4622,
    '16': 3302,
    '17': 3753,
    '18': 3287,
    '19': 3112
}

class_select_dict = {
    '1': 3702,
    '2': 3022,
    '3': 4122,
    '4': 4502,
    '5': 2820,
    '6': 3403,
    '7': 3202,
    '8': 4622,
    '9': 3302,
    '10': 3753,
    '11': 3287,
    '12': 3112
}


# This is the index page
@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template('index.html')

# User page that will display the user's course schedule
@app.route('/user/<username>')
@login_required
def user(username):

    # Default user id set to -1
    user_id = -1

    if current_user.is_authenticated:
        user = current_user.username
        user_object = User.query.filter_by(username=user).first()
        user_id = user_object.return_id()
        
        # user_sched= SemesterSchedule.query.all()
        user_sched = SemesterSchedule.query.filter_by(user_id=user_id).all()

        # From Emily: ["That's it!"] = "You've taken all the courses you need to graduate."
        sched_list = []
        for plan in user_sched:
            # split courses into a list of 1 each
            class_list = plan.classlist.split()
            if class_list[0] == "You've":
                # deleting list using clear()
                class_list.clear()
                class_list.append("That's it! You've taken all the courses you need to graduate.")
            else:
                for c in class_list:
                    c = "CSPB" + " " + str(c)
            class_list.insert(0, plan.semester)
            sched_list.append(class_list)
        '''
            review = {
                "Semester": plan.semester,
                "Classes": class_list
            }
            sched_list.append(review)
        '''
        # return str(sched_list)
        return render_template('user.html', schedule=sched_list)



# This was removed but might be added later
@app.route('/about')
def about():
    user = {'username': 'Ryan'}
    return render_template('about.html')


@app.route('/plan', methods=['GET', 'POST'])
@app.route('/plan')
@login_required
def plan():

    # Default user id set to -1
    user_id = -1
    # form = PlanForm()
    # Get the id of the current user that is logged in
    if current_user.is_authenticated:
        user = current_user.username
        user_object = User.query.filter_by(username=user).first()
        user_id = user_object.return_id()

    # if form.validate_on_submit():
    if request.method == 'POST':
        # mycheckbox is Classes already taken
        selected_list = request.form.getlist('mycheckbox')
        selected_class = [class_dict[x] for x in selected_list]
        hours = int(request.form.getlist('hour_to_have')[0])
        elective = request.form.getlist('mycheckbox_elect')
        semester = request.form.getlist('mycheckbox_semester')
        dontwant = request.form.getlist('mycheckbox_not')
        # The two lists below need to be integers to work
        for i in range(0, len(semester)):
            semester[i] = int(semester[i])
        for i in range(0, len(dontwant)):
            dontwant[i] = int(dontwant[i])
        for i in range(0, len(elective)):
            elective[i] = int(elective[i])

        # Testing the return values from Emily's algorithm
        # strr = "Selected classes:" + str(selected_class) + " " + "Hours:" + str(hours) + " " + "Electives:" + str(elective) + " " + "Semester:" + str(semester) + " " + "Don't want:" + str(dontwant)
        # return strr
        # Delete all of the old classes for this user
        SemesterSchedule.query.filter_by(user_id=user_id).delete()

        classes = multipleSemesters(selected_class, hours, elective, semester, dontwant)
        classes2 = dict()
        for c in classes:
            if c == 0: 
                classes2["Summer 2022"] = classes[c]
            elif c == 1:
                classes2["Fall 2022"] = classes[c]
            elif c == 2: 
                classes2["Spring 2023"] = classes[c]
            elif c == 3: 
                classes2["Summer 2023"] = classes[c]
            elif c == 4: 
                classes2["Fall 2023"] = classes[c]
            else: 
                classes2["Spring 2024"] = classes[c]


        for c in classes2:
            semester = c
            class_list = classes2[c]

            classes_string = ""
            for c in class_list:
                # ["That's it!"] = "You've taken all the courses you need to graduate." == "You've taken all the courses you need to graduate."):
                print(c)
                if (str(c)[0] == "Y"):
                    classes_string = "You've taken all the courses you need to graduate."
                    # Yes I know break is bad programming practice; will update later
                    break
                else:
                    classes_string = str(c) + " " + classes_string
            # print(classes_string)
            # if its "you graduated do something different
            # hours is hours per week
            # user_id is the user's id
            # get the timestamp
            ts = datetime.datetime.utcnow()
            plan = SemesterSchedule(semester=semester, classlist=classes_string, hoursperweek=hours, timestamp=ts, user_id=user_id)
            db.session.add(plan)
            db.session.commit()
        # return classes_string
        #redirect after posting review to user's page
        return redirect('/user/<username>')
    else:
        return render_template('plan.html')

@app.route('/contact', methods=['GET', 'POST'])
@app.route('/contact')
def contact():
    user = {'username': 'Ryan'}
    return render_template('contact.html', user=user)


# This was never implemented fully
@app.route('/updates')
# @app.route decorators from Flask, the function becomes protected 
# and will not allow access to users that are not authenticated
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
# @app.route decorators from Flask, the function becomes protected 
# and will not allow access to users that are not authenticated
@login_required
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
        review = {
            "Class": review.classname,
            "Hours per week": review.hoursperweek,
            "Review": review.review,
            "Stars":review.stars
           }
        reviews_list.append(review)
    # return str(reviews_list)
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

