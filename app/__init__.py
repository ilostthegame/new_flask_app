## This __init__.py file makes it into a package.
## This executes and defines what symbols the package exposes to
## the outside world, when imported.

from flask import Flask

app = Flask(__name__)  # __name__ is set to name of module (file).
# This is a global variable within the package.

from app import routes  # This is importing from the directory 'app'


