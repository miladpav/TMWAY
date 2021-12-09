from flask_wtf import FlaskForm

from wtforms import TextAreaField, SubmitField, PasswordField, StringField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()], render_kw={"placeholder": "Username ..."})
    password = PasswordField(label="Password", validators=[DataRequired()], render_kw={"placeholder": "Password ..."})
    firstName = StringField(label="FirstName", validators=[DataRequired()], render_kw={"placeholder": "First Name ..."})
    lastName = StringField(label="LastName", validators=[DataRequired()], render_kw={"placeholder": "Last Name ..."})
    submit = SubmitField('Submit your data')
    