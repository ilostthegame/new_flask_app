## This __init__.py file makes it into a package.
## This executes and defines what symbols the package exposes to
## the outside world, when imported.

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# This is a global variable within the package.
app = Flask(__name__)  # __name__ is set to name of module (file).
# Using method that sets app config. Note that app.config is 
# the config module.
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models  # This is importing from the directory 'app'
