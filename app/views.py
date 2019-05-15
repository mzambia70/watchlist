from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    view root page function that returnsthe index page and its data

    '''
    message = 'my movies'
    return render_template('index.html',message = message)