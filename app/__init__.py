from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from flask_migrate import Migrate


app = Flask(__name__)
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


login = LoginManager(app)
login.login_view = 'login'

from app import routes, models