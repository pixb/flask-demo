from flask import Flask
import config
app = Flask(__name__)
# 第一种方式
app.config.from_object(config)

# 第二种方式
app.config.from_pyfile("config.py")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
