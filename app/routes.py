from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Bob'}
    posts = [
        {
            'author': {'username': 'hi 1'},
            'body': 'eeee!'
        },
        {
            'author': {'username': 'wwww 2'},
            'body': 'daf!'
        }
    ]
    return render_template('index.html', 
                           title='Home', 
                           user=user, 
                           posts=posts)

# Testing page
@app.route('/test')
def test_page():
    return render_template('test.html',
                           t="hello")

# Login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Displays message to webpage.
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))  # Redirects user to index.
    # Rendering template, and passing in the form object
    # which contains all the HTML stuff
    return render_template('login.html', title='Sign In', form=form)

# GET requests return information to the client, while POST requests
# are usually used when browser submits form data to server.

