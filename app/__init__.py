# the app will start to run instances of this script

from flask import Flask
'''
created by: denz 04/27/2017
'''
app = Flask(__name__, instance_relative_config=True)

# Load views
from app import views

# Load config files
app.config.from_object('config.config')
