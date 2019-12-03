from flask import Flask,jsonify
from json import JSONEncoder

app = Flask(__name__)

class Student:
    age = 0
    name=""
    def __init__(self,age,name):
        self.age = age
        self.name = name

class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

def get_all_users():
    user_list = []
    user_list.append(Student(11,"xiaoming"))
    user_list.append(Student(22,"Jams"))
    user_list.append(Student(33,"Anthony"))
    user_list.append(Student(44,"Bosh"))
    return user_list

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

# response users api,use jsonify
@app.route('/users/')
def users_api():
    users = get_all_users()

    # return jsonify(json.dump(users))
    return MyEncoder().encode(users)

if __name__ == '__main__':
    app.run(debug=True)
