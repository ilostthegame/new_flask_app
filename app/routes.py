from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'sigma'}
    posts = [
        {
            'author': {'username': 'RIzzler 1'},
            'body': 'skibidi ohio rizzlers skibi gyatt rizz!'
        },
        {
            'author': {'username': 'riuzLer 2'},
            'body': 'skibi skibi skibi dop dop dop!'
        }
    ]
    return render_template('index.html', 
                           title='Home', 
                           user=user, 
                           posts=posts)


@app.route('/skibidi')
def easter_egg():
    cool_msg = "bing bong"
    return render_template('skibidi.html', msg=cool_msg)

