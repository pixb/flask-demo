from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__='roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    users=db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role {}>'.format(self.name)

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(64),unique=True,index=True)
    role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User {}'.format(self.username)

def hello_world():
    return 'Hello World!'

@app.route('/adduser/')
def add_user():
    db.session.add(User("zhangsan"))
    db.session.add(User("scott"))
    db.session.add(User("Jams"))
    db.session.add(User("Wade"))
    db.session.add(User("hart"))
    db.session.add(User("marin"))
    db.session.add(User("thethy"))
    db.session.commit()
    return "add all user success!"

if __name__ == '__main__':
    app.run()
