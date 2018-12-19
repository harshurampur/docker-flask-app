#################
#### imports ####
#################
from flask import Flask
from .config import app_config
import os

################
#### config ####
################
env_name = os.getenv('FLASK_ENV')
app = Flask(__name__)
app.config.from_object(app_config[env_name])

from . import view