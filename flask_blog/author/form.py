from flask_wtf import  Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
    fullname = StringField('Full Name', [validators.required()])
    email = EmailField('Email', [validators.required()])
    username = StringField('Username', [
        validators.required(),
        validators.length(min=4, max=25)
    ])
    Password = PasswordField('New Password',[
        validators.required(),
        validators.equal_to('Confirm', message="Password must match"),
        validators.length(min=4, max=80)
    ])
    confirm = PasswordField('Repeat Password')