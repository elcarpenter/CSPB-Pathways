from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config
from flask_migrate import Migrate


app = Flask(__name__)
# Fixed warning when flask starts
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)
# add secret key to config file later
app.config['SECRET_KEY'] = 'any secret string'
db = SQLAlchemy(app)
# Migration is for migrating database changes in models.py
migrate = Migrate(app, db)

# https://stackoverflow.com/questions/44941757/sqlalchemy-exc-operationalerror-sqlite3-operationalerror-no-such-table
@app.before_first_request
def create_tables():
    db.create_all()

# This redirects to the login page if you are trying to access a
# page you need to be logged into
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models