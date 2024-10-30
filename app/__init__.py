## This __init__.py file makes it into a package.
## This executes and defines what symbols the package exposes to
## the outside world, when imported.

from flask import Flask
from config import Config

# This is a global variable within the package.
app = Flask(__name__)  # __name__ is set to name of module (file).
# Using method that sets app config. Note that app.config is 
# the config module.
app.config.from_object(Config)  

from app import routes  # This is importing from the directory 'app'
