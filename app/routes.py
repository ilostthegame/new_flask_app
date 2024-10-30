from flask import render_template, flash, redirect
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

# Login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')  # Redirects user to index.
    # Rendering template, and passing in the form object
    # which contains all the HTML stuff
    return render_template('login.html', title='Sign In', form=form)

# GET requests return information to the client, while POST requests
# are usually used when browser submits form data to server.

# TODO: Test GET request with form submitting data to server.
