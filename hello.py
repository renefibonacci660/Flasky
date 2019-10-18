#!/usr/bin/python3

from flask import Flask, redirect, abort, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/bassets')
def bassets():
    return redirect('https://www.youtube.com/watch?v=Thb0NHX7jc8&feature=youtu.be')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/users/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}!</h1>'.format(user.name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
