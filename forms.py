from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# we could write that stuff in the main.py file but it's better to separate
# this into it's own file (easier to update later)


# creating form for registration, we need to inherit from FlaskForm
# we will create forms by writing python classes which will be later converted
# into an html forms within our template
class RegistrationForm(FlaskForm):
    # within our form, we need to create form fields (also classes) which
    # we will need to import from wtforms
    # validators in our fields are a list of limitations that are applied
    # to that field
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
