from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_script import Shell, Manager
from flask_migrate import Migrate, MigrateCommand

"""
这个Demo用来实现校验用户的密码的Demo
简单的实现一个用户注册与登录功能
"""

app = Flask(__name__)
manager = Manager(app)

# 配置数据库,sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True

# 数据库相关j
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# 用户数据模型
# 实现用户密码生成与校验功能，引入werkzeug
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        """
        设置用户的密码
        :param password:
        :return:
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        校验用户的密码
        :param password:
        :return:
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """
    注册接口
    :return:
    """
    username = request.args.get('username')
    password = request.args.get('password')
    if username is None:
        return "username is Null"

    if password is None:
        return "password is Null"

    user = User.query.filter_by(username=username).first()
    if user is not None:
        return "user exists!"

    # insert new user to database
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return "register success,{}".format(new_user.username)


@app.route('/login/')
def login():
    """
    登录接口
    :return:
    """

    username = request.args.get('username')
    password = request.args.get('password')
    if username is None:
        return "username is Null"

    if password is None:
        return "password is Null"

    user = User.query.filter_by(username=username).first()
    if user is None:
        return "user is not exists!"

    if user.verify_password(password):
        return "login success!Welcome {}".format(user.username)
    else:
        return "login error,password is error!"


# 导入shell
def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
