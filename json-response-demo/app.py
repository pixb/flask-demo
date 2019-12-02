from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/json/')
def python_resp():
    return {
        "username":"Tom",
        "age":33,
        "isadmin":True,
        "nullobjj":None
    }

# TODO:response users api,use jsonify

if __name__ == '__main__':
    app.run()
