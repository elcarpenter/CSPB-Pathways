from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# Flask-Login keeps track of the logged in user by storing its unique identifier in Flask's user session
# When logged-in user navigates to a new page, Flask-Login retrieves the ID of the user from the session and then loads that user into memory.
@login.user_loader
def load_user(id):
    try:
        return User.query.get(int(id))
    except:
        return None


# change form to student later
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def return_id(self):
        return self.id

    def __repr__(self):
        return '<User {}>'.format(self.username)

# Class reviews from Users
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classname = db.Column(db.String(40))
    hoursperweek = db.Column(db.Integer)
    review = db.Column(db.String(200))
    stars = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Review {}>'.format(self.classname)
        # return '<Review {}>'.format(self.classname, hoursperweek, self.review, self.stars, self.timestamp) 

# Semester Schedule for the User
class SemesterSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    semester = db.Column(db.String(60), index=True)
    classlist = db.Column(db.String(60), index=True)
    hoursperweek= db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<SemesterSchedule {} >'.format(self.user_id)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


