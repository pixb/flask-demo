from flask import Flask,render_template,request

app = Flask(__name__)

# templates test demo
@app.route('/',methods=['GET','POST'])
@app.route('/<name>',methods=['GET','POST'])
def hello_world(name=None):
    return render_template('hello.html',name=name)


if __name__ == '__main__':
    app.run(debug=True)

with app.test_request_context('/',method='POST'):
    assert request.method == 'GET'
    assert request.path == '/hello'
