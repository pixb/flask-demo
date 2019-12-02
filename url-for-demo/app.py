from flask import Flask,escape,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/list/')
def my_list():
    return "my list!"
@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('my_list'))
    print(url_for('login',next='/'))
    print(url_for('profile',username='John Doe'))

if __name__ == '__main__':
    app.run(debug=True)
