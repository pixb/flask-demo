from flask import Flask,render_template

app = Flask(__name__)

# templates test demo
@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template('hello.html',name=name)


if __name__ == '__main__':
    app.run(debug=True)
