from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, NumberRange
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class ReviewForm(FlaskForm):
    classname = SelectField(
        'Class Number',
        [DataRequired()],
        choices=[
            ('CSPB 1300', 'CSPB 1300'),
            ('CSPB 2824', 'CSPB 2824'),
            ('CSPB 2270', 'CSPB 2270'),
            ('CSPB 3104', 'CSPB 3104'),
            ('CSPB 2400', 'CSPB 2400'),
            ('CSPB 3308', 'CSPB 3308'),
            ('CSPB 3155', 'CSPB 3155'),
            ('CSPB 3702', 'CSPB 3702'),
            ('CSPB 3022', "CSPB 3022"),
            ('CSPB 4122', "CSPB 4122"),
            ('CSPB 4502', "CSPB 4502"),
            ('CSPB 2820', "CSPB 2820"),
            ('CSPB 3403', "CSPB 3403"),
            ('CSPB 3753', 'CSPB 3753'),
            ('CSPB 3287', "CSPB 3287"),
            ('CSPB 4622', "CSPB 4622"),
            ('CSPB 3302', "CSPB 3302"),
            ('CSPB 3203', "CSPB 3202")
        ]
    )
    review = TextAreaField('Please enter your review:', validators=[DataRequired()])
    hoursPerWeek = IntegerField('Hours per week', validators=[DataRequired(), NumberRange(min=0, message='Must enter a number greater than 0')])
    stars = SelectField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'),('5', '5')])
    submit = SubmitField('Send Review')
    


class PlanForm(FlaskForm):
    classesTaken = SelectField(
        'Class Number',
        [DataRequired()],
        choices=[
            ('CSPB 1300', 'CSPB 1300'),
            ('CSPB 2824', 'CSPB 2824'),
            ('CSPB 2270', 'CSPB 2270'),
            ('CSPB 3104', 'CSPB 3104'),
            ('CSPB 2400', 'CSPB 2400'),
            ('CSPB 3308', 'CSPB 3308'),
            ('CSPB 3155', 'CSPB 3155'),
            ('CSPB 3702', 'CSPB 3702'),
            ('CSPB 3022', "CSPB 3022"),
            ('CSPB 4122', "CSPB 4122"),
            ('CSPB 4502', "CSPB 4502"),
            ('CSPB 2820', "CSPB 2820"),
            ('CSPB 3403', "CSPB 3403")
        ]
    )
    hoursPerWeek = IntegerField('Hours per week', validators=[DataRequired(), NumberRange(min=0, message='Must enter a number greater than 0')])
    electives = SelectField(
        'Class Number',
        [DataRequired()],
        choices=[
            ('CSPB 3702', 'CSPB 3702'),
            ('CSPB 3022', "CSPB 3022"),
            ('CSPB 4122', "CSPB 4122"),
            ('CSPB 4502', "CSPB 4502"),
            ('CSPB 2820', "CSPB 2820"),
            ('CSPB 3403', "CSPB 3403")            
        ]
    )
    semester = SelectField(
        'Semester',
        [DataRequired()],
        choices=[
            ('Summer 2022', 'Summer 2022'),
            ('Fall 2022', 'Fall 2022'),
            ('Spring 2023', 'Spring 2023'),
            ('Summer 2023', 'Summer 2023'),
            ('Fall 2023', 'Fall 2023'),
            ('Spring 2024', 'Spring 2024'),
        ]
    )
    notTake = SelectField(
        'Class Number',
        [DataRequired()],
        choices=[
            ('CSPB 1300', 'CSPB 1300'),
            ('CSPB 2824', 'CSPB 2824'),
            ('CSPB 2270', 'CSPB 2270'),
            ('CSPB 3104', 'CSPB 3104'),
            ('CSPB 2400', 'CSPB 2400'),
            ('CSPB 3308', 'CSPB 3308'),
            ('CSPB 3155', 'CSPB 3155'),
            ('CSPB 3702', 'CSPB 3702'),
            ('CSPB 3022', "CSPB 3022"),
            ('CSPB 4122', "CSPB 4122"),
            ('CSPB 4502', "CSPB 4502"),
            ('CSPB 2820', "CSPB 2820"),
            ('CSPB 3403', "CSPB 3403")
        ]
    )
    submit = SubmitField('Send Review')

