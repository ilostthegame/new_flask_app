## This __init__.py file makes it into a package.
## This executes and defines what symbols the package exposes to
## the outside world, when imported.

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)  # __name__ is set to name of module (file).
# Using method that sets app config.
app.config.from_object(Config)
db = SQLAlchemy(app)  # Represents a database object
migrate = Migrate(app, db)  # Represents the database migration engine

from app import routes, models
