from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

def my_list():
    return '我是列表项'

app.add_url_rule('/list/',endpoint='zhiliao',view_func=my_list)

if __name__ == '__main__':
    app.run()
