from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    a = 1
    b = 0
    c = a/b
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
    # 开启Debug模式，方便在页面中看到错误信息
    # 更改代码会自动加载
    # app.run()
