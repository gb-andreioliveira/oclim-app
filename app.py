#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_main():
    return 'Welcome to the initial page!\n'

@app.route('/hello/')
def hello_world():
    return 'Hello World!\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Hey there %s!\n' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)     # open for everyone