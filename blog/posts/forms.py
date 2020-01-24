from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_ckeditor import CKEditorField


class PostForm(FlaskForm):
    """This Class Handles Post Form""" 
    title = StringField('Title', validators=[DataRequired(), Length(min=5, max=150)])
    subtitle = StringField('Subtitle', validators=[DataRequired(), Length(min=10, max=500)])
    author = StringField('Author', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    article = CKEditorField('Article', validators=[DataRequired()])
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    """This class handles the comment form"""
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    website = StringField('Website')
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post')