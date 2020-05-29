from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'


@app.route('/hello')
def hello_world():
    return "hello world!"


@app.route('/name')
def get_name():
    return {"name": "asdf"}


@app.route('/name/<username>')
def show_name(username):
    return "username %s" % escape(username)
