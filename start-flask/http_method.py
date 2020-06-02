import json

from flask import Flask, request, abort, redirect, url_for

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 接受json类型数据
        data = request.get_data()
        print(data)
        json_data = json.loads(data.decode("utf-8"))
        print(json_data.get('a'))
        print(json_data.get('b'))

        return "do login"
    else:
        # GET 请求数据接受方式
        print(request.args.get('name'))
        print(request.args.get('age'))
        return "show login html"


@app.route('/login2', methods=['POST'])
def login2():
    # 接受表单FORM数据
    if request.method == 'POST':
        data = request.form
        print(data.get('a'))
        print(data.get('b'))
        return 'success'
    return "Invalid request method"


@app.route('/error')
def error_response():
    abort(401)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.errorhandler(404)
def error_404_response(error):
    return '404 response is there: {}'.format(error)


@app.errorhandler(Exception)
def error_exception_response(error):
    # /error 401 在这里会被捕获
    return 'exception: {}'.format(error)