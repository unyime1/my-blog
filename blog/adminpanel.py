"""This module handles the admin panel"""

from blog import db
from blog import admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from blog.models import User, Post, ContactUs, Comment
from flask_login import current_user 


class MyModelView(ModelView):
     def is_accessible(self):     
         # this function controls access to the admin page views    
        return current_user.is_authenticated and current_user.admin == True 

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):        
        # this function controls access to the admin index view 
        return current_user.is_authenticated and current_user.admin == True  


admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Post, db.session))
admin.add_view(MyModelView(ContactUs, db.session))
admin.add_view(MyModelView(Comment, db.session))

