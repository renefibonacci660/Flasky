#!/usr/bin/python3

from flask import Flask, redirect, abort
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/bassets')
def bassets():
    return redirect('https://www.youtube.com/watch?v=Thb0NHX7jc8&feature=youtu.be')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/users/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}!</h1>'.format(user.name)

