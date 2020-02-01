"""This module handles the contact form"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    """This Class Handles Contact Us Form""" 
    name = StringField('Name', validators=[DataRequired(), Length(min=5, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired(), Length(min=10, max=300)])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit') 