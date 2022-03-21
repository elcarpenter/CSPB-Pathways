from flask import Flask
from flask import render_template
from flask import request
import json

from basicGen import basicAlg
from reviews import *


app = Flask(__name__)

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

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    user = {'username': 'Ryan'}
    return render_template('index.html', user=user)

@app.route('/about')
def about():
    user = {'username': 'Ryan'}
    return render_template('about.html', user=user)

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

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    if request.method == 'POST':
        selected_list = request.form.getlist('mycheckbox')
        reviews = review_printer(selected_list)
        return render_template('reviews.html', reviews=reviews)
    else:
        reviews = {}
        return render_template('reviews.html', reviews=reviews)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

