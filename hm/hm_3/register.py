from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import data_required, Email, EqualTo, ValidationError

class RegisterForm(FlaskForm):
    first_name = StringField('first name', validators=[data_required(data_required)])
    last_name = StringField('last name', validators=[data_required(data_required)])
    password = PasswordField('password', validators=[data_required()])
    confirm_password = PasswordField('Confirm password',
                                     validators=[data_required(data_required), EqualTo('password')])
    email = StringField('email', validators=[data_required(), Email()])

