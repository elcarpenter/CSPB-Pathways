from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def index():
    user = {'username': 'Ryan'}
    return render_template('index.html', user=user)

@app.route('/about')
def about():
    user = {'username': 'Ryan'}
    return render_template('about.html', user=user)

@app.route('/plan')
def plan():
    user = {'username': 'Ryan'}
    return render_template('plan.html', user=user)

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

