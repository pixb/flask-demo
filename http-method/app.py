from flask import Flask,request

app = Flask(__name__)

# test http method
@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        return 'POST METHOD:hello world!'
    else:
        return 'GET METHOD:Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
