from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired, Length, Email
from wtforms import StringField, TextAreaField, SubmitField


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10)])
    recaptcha = RecaptchaField()