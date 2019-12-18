from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager


app = Flask(__name__)

# 赋值数据库的路径
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/users.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True
db = SQLAlchemy(app)


class Role(db.Model):
    """角色的模型"""
    # 表名称
    __tablename__ = 'roles'
    # 主键
    id = db.Column(db.Integer, primary_key=True)
    # unique 不能重复
    name = db.Column(db.String(64), unique=True)

    # 角色的所有用户,返回该角色的所有用户的列表
    # relationship,参数1：另一端的模型
    # backref：向对方User模型添加一个role属性，从而定义反向关系。可以代替外键访问Role对象
    users = db.relationship('User', backref='role')

    # 动态关系，user将不再直接返回结果，而是返回一个动态未执行查询，需要调用all()，first()等进行查询
    # 中间可以添加过滤器等相关操作
    # users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role {}>'.format(self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # roles表中的id字段作为外键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User {}'.format(self.username)


@app.route('/')
def hello_world():
    return 'Hello World!'


admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_david = User(username='david', role=user_role)


@app.route('/adduser/')
def add_user():
    db.session.add(admin_role)
    db.session.add(mod_role)
    db.session.add(user_role)
    db.session.add(user_john)
    db.session.add(user_susan)
    db.session.add(user_david)
    db.session.commit()
    db.session.delete(mod_role)
    db.session.commit()
    return "add all user success!"


@app.route('/role_list/')
def role_list():
    """查询所有角色"""
    r = Role.query.all()
    print(r)
    return "role_list"


@app.route('/user_list/')
def user_list():
    """查询所有用户"""
    ru = User.query.all()
    print(ru)
    return "user_list"


@app.route('/user_role_list')
def user_role_list():
    """查询所有user_role的用户"""
    r = Role.query.filter_by(name='User').first()
    users = r.users
    print(users)
    return "user_role_list"


manager = Manager(app)

# migrate 数据库迁移
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# 自动导入对象
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
