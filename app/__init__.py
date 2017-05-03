# the app will start to run instances of this script

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

"""
created by: denz 04/27/2017
"""
# local imports
from config import app_config


# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    # Load config files
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # login manager
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"


    return app
