from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Harrison'}
    posts = [
        {
            'author' : {'username' : 'Joey'},
            'body': 'This is a post.'
        },
        {
            'author': {'username': 'Henry'},
            'body': 'This is another post.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
