"""This Module Handles the database models"""

from datetime import datetime
from blog import db, login_manager 
from flask_login import UserMixin, current_user 


@login_manager.user_loader
def load_user(user_id):
    """Used to find users from the database by id"""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """This Class Handles the Admin User"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    admin = db.Column(db.Boolean, default=False)

    def is_admin(self):        
        return self.admin

    def __repr__(self):
        return f"User('{self.username}', '{self.password}', {self.date_created}')"


class Post(db.Model):
    """This class handles the posts model"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String, index=True)
    subtitle = db.Column(db.String(500), nullable=False)
    author = db.Column(db.String(), nullable=False)
    link = db.Column(db.String(), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    article = db.Column(db.Text, nullable=False)
    comment = db.relationship('Comment', backref='post', lazy='dynamic')


    def __repr__(self):
       return f"Post('{self.title}', '{self.subtitle}', '{self.author}', '{self.link}', '{self.date_posted}')"


class ContactUs(db.Model):
    """This class handles the contact us model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(300), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Contact('{self.name}', '{self.email}', '{self.subject}', '{self.date}', {self.message})"

class Comment(db.Model):
    """This class handles comments"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    website = db.Column(db.String(100))
    content = db.Column(db.Text, nullable=False)
    comment_reply = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    



from blog.adminpanel import * 