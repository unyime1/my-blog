"""This module houses the application factory"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_ckeditor import CKEditor
from blog.config import Config
from flask_admin import Admin
from flask_login import LoginManager
from flask_share import Share


db = SQLAlchemy()
ckeditor = CKEditor()
admin = Admin()
migrate = Migrate()
share = Share()



login_manager = LoginManager()
login_manager.login_view = 'main.home'
login_manager.login_message_category = 'info'


from blog.models import MyAdminIndexView


def create_app(config_class=Config):
    """Application Factory"""
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app, index_view=MyAdminIndexView())
    ckeditor.init_app(app)
    login_manager.init_app(app)
    share.init_app(app)

    from blog.main.routes import main
    from blog.posts.routes import posts
    from blog.users.routes import users
    from blog.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(users)
    app.register_blueprint(errors)

    return app

manager = Manager(create_app)
manager.add_command('db', MigrateCommand)