> 大型项目模板

# 说明

这个工程来创建一个标准大型工程的模板。参考到自《基于Python的Web应用开发实战》

# 大型项目的结构

## 1、项目结构

多文件 Flask 程序的基本结构

```css
|-flasky
	|-app/
		|-templates/
		|-static/
		|-main/
			|-__init__.py
			|-errors.py
			|-forms.py
			|-views.py
		|-__init__.py
		|-email.py
		|-models.py
	|-migrations/
	|-tests/
		|-__init__.py
		|-test*.py
	|-venv/
	|-requirements.txt
	|-config.py
	|-manage.py

```

这种结构有 4 个顶级文件夹:
• Flask 程序一般都保存在名为 `app` 的包中;
• 和之前一样,`migrations` 文件夹包含数据库迁移脚本;
• 单元测试编写在 `tests` 包中;
• 和之前一样,`venv` 文件夹包含 `Python` 虚拟环境。
同时还创建了一些新文件:
• `requirements.txt` 列出了所有依赖包,便于在其他电脑中重新生成相同的虚拟环境;
• `config.py` 存储配置;
• `manage.py` 用于启动程序以及其他的程序任务。
为了帮助你完全理解这个结构,下面几节讲解把 `hello.py` 程序转换成这种结构的过程。

## 2、配置选项

程序经常需要设定多个配置。这方面最好的例子就是开发、测试和生产环境要使用不同的
数据库,这样才不会彼此影响。

我们不再使用 `hello.py` 中简单的字典状结构配置,而使用层次结构的配置类。

`config.py` 文件的内容如示例 所示。

```css
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
	
	@staticmethod
	def init_app(app):
		pass
		
class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
		
class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
	
class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
		'sqlite:///' + os.path.join(basedir, 'data.sqlite')
		
config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}

```

基类 Config 中包含通用配置,子类分别定义专用的配置。如果需要,你还可添加其他配置类。

为了让配置方式更灵活且更安全,某些配置可以从环境变量中导入。例如, `SECRET_KEY` 的值,这是个敏感信息,可以在环境中设定,但系统也提供了一个默认值,以防环境中没有定义。

在 3 个子类中,`SQLALCHEMY_DATABASE_URI` 变量都被指定了不同的值。这样程序就可在不同的配置环境中运行,每个环境都使用不同的数据库。

配置类可以定义 `init_app()` 类方法,其参数是程序实例。在这个方法中,可以执行对当前环境的配置初始化。现在,基类 `Config` 中的 `init_app() `方法为空。

在这个配置脚本末尾,config 字典中注册了不同的配置环境,而且还注册了一个默认配置
(本例的开发环境)。

## 3、程序包

程序包用来保存程序的所有代码、模板和静态文件。我们可以把这个包直接称为 app(应用),如果有需求,也可使用一个程序专用名字。templates 和 static 文件夹是程序包的一部分,因此这两个文件夹被移到了 app 中。数据库模型和电子邮件支持函数也被移到了这个包中,分别保存为 app/models.py 和 app/ATABASE_URL 中读取,如果没有定义这个环境变量,则使用名为`data-dev.sqlite` 的 `SQLite` 数据库。
不管从哪里获取数据库 URL,都要在新数据库中创建数据表。

如果使用 Flask-Migrate 跟踪迁移,可使用如下命令创建数据表或者升级到最新修订版本:

```css
(venv) $ python manage.py db upgrade
```



不管你是否相信,第一部分到此就要结束了。现在你已经学到了使用 Flask 开发 Web 程序
的必备基础知识,不过可能还不确定如何把这些知识融贯起来开发一个真正的程序。本书
第二部分的目的就是解决这个问题,带着你一步一步地开发出一个完整的程序。
known=session.get('known', False),
							current_time=datetime.utcnow())

```

在蓝本中编写视图函数主要有两点不同:

- 第一,和前面的错误处理程序一样,路由修饰器由蓝本提供;
- 第二,`url_for()` 函数的用法不同。

你可能还记得,`url_for()` 函数的第一个参数是路由的端点名,在程序的路由中,默认为视图函数的名字。

例如,在单脚本程序中,index() 视图函数的 URL 可使用 url_for('index') 获取。
在蓝本中就不一样了,Flask 会为蓝本中的全部端点加上一个命名空间,这样就可以在不同的蓝本中使用相同的端点名定义视图函数,而不会产生冲突。

命名空间就是蓝本的名字(Blueprint 构造函数的第一个参数),所以视图函数 index() 注册的端点名是 main.index,
其 URL 使用 url_for('main.index') 获取。

url_for() 函数还支持一种简写的端点形式,在蓝本中可以省略蓝本名,例如 url_for('.index')。在这种写法中,命名空间是当前请求所在的蓝本。这意味着同一蓝本中的重定向可以使用简写形式,但跨蓝本的重定向必须使用带有命名空间的端点名。
为了完全修改程序的页面,表单对象也要移到蓝本中,保存于 app/main/forms.py 模块。

## 4、启动脚本

顶级文件夹中的 `manage.py` 文件用于启动程序。脚本内容如示例

` manage.py`:启动脚本

​```python
#!/usr/bin/env python
import os
from app import create_app, db
from app.models import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
manager.run()

```

这个脚本先创建程序。如果已经定义了环境变量 `FLASK_CONFIG`,则从中读取配置名;否则使用默认配置。

然后初始化 `Flask-Script`、`Flask-Migrate` 和为 `Python shell` 定义的上下文。

出于便利,脚本中加入了 shebang 声明,所以在基于 Unix 的操作系统中可以通过 `./manage.py` 执行脚本,而不用使用复杂的 `python manage.py`。

## 4、需求文件

程序中必须包含一个 `requirements.txt` 文件,用于记录所有依赖包及其精确的版本号。如果要在另一台电脑上重新生成虚拟环境,这个文件的重要性就体现出来了,例如部署程序时使用的电脑。pip 可以使用如下命令自动生成这个文件:

```css
(venv) $ pip freeze >requirements.txt
```

安装或升级包后,最好更新这个文件。需求文件的内容示例如下:

```css
Flask==0.10.1
Flask-Bootstrap==3.0.3.1
Flask-Mail==0.9.0
Flask-Migrate==1.1.0
Flask-Moment==0.2.0
Flask-SQLAlchemy==1.0
Flask-Script==0.6.6
Flask-WTF==0.9.4
Jinja2==2.7.1
Mako==0.9.1
MarkupSafe==0.18
SQLAlchemy==0.8.4
WTForms==1.0.5
Werkzeug==0.9.4
alembic==0.6.2
blinker==1.3
itsdangerous==0.23

```

如果你要创建这个虚拟环境的完全副本,可以创建一个新的虚拟环境,并在其上运行以下
命令:

```css
(venv) $ pip install -r requirements.txt
```

当你阅读本书时,该示例 `requirements.txt` 文件中的版本号可能已经过期了。如果愿意,你可以试着使用这些包的最新版。如果遇到问题,你可以随时换回这个需求文件中的版本,因为这些版本和程序兼容。

## 5、单元测试

这个程序很小,所以没什么可测试的。不过为了演示,我们可以编写两个简单的测试。

示例：` tests/test_basics.py`:单元测试

```css
import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		db.create_all()
		
	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()
		
	def test_app_exists(self):
		self.assertFalse(current_app is None)
		
	def test_app_is_testing(self):
		self.assertTrue(current_app.config['TESTING'])


```

这个测试使用 Python 标准库中的 unittest 包编写。setUp() 和 tearDown() 方法分别在各测试前后运行,并且名字以 test_ 开头的函数都作为测试执行。

`setUp()` 方法尝试创建一个测试环境,类似于运行中的程序。首先,使用测试配置创建程序,然后激活上下文。这一步的作用是确保能在测试中使用 current_app,像普通请求一样。然后创建一个全新的数据库,以备不时之需。数据库和程序上下文在 tearDown() 方法中删除。

第一个测试确保程序实例存在。第二个测试确保程序在测试配置中运行。若想把 tests 文件夹作为包使用,需要添加 `tests/__init__.py `文件,不过这个文件可以为空,因为 unittest包会扫描所有模块并查找测试。

为了运行单元测试,你可以在 manage.py 脚本中添加一个自定义命令。

示例 展示了如何添加 test 命令。

`manager.py`:启动单元测试的命令

```python
@manager.command
def test():
	"""Run the unit tests."""
	import unittest
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)

```

`manager.command` 修饰器让自定义命令变得简单。修饰函数名就是命令名,函数的文档字符串会显示在帮助消息中。test() 函数的定义体中调用了 unittest 包提供的测试运行函数。
单元测试可使用下面的命令运行:

```css
(venv) $ python manage.py test
test_app_exists (test_basics.BasicsTestCase) ... ok
test_app_is_testing (test_basics.BasicsTestCase) ... ok

.----------------------------------------------------------------------
Ran 2 tests in 0.001s
OK

```

## 6、创建数据库

重组后的程序和单脚本版本使用不同的数据库。

首选从环境变量中读取数据库的 URL,同时还提供了一个默认的 SQLite 数据库做备用。

3种配置环境中的环境变量名和 SQLite BASE_URL 中读取,如果没有定义这个环境变量,则使用名为`data-dev.sqlite` 的 `SQLite` 数据库。
不管从哪里获取数据库 URL,都要在新数据库中创建数据表。

如果使用 Flask-Migrate 跟踪迁移,可使用如下命令创建数据表或者升级到最新修订版本:

```css
(venv) $ python manage.py db upgrade
```



不管你是否相信,第一部分到此就要结束了。现在你已经学到了使用 Flask 开发 Web 程序
的必备基础知识,不过可能还不确定如何把这些知识融贯起来开发一个真正的程序。本书
第二部分的目的就是解决这个问题,带着你一步一步地开发出一个完整的程序。数据库文件名都不一样。例如,在开发环境中,数据库 URL 从环境变量 DEV_DATABASE_URL 中读取,如果没有定义这个环境变量,则使用名为`data-dev.sqlite` 的 `SQLite` 数据库。
不管从哪里获取数据库 URL,都要在新数据库中创建数据表。

如果使用 Flask-Migrate 跟踪迁移,可使用如下命令创建数据表或者升级到最新修订版本:

```css
(venv) $ python manage.py db upgrade
```



不管你是否相信,第一部分到此就要结束了。现在你已经学到了使用 Flask 开发 Web 程序
的必备基础知识,不过可能还不确定如何把这些知识融贯起来开发一个真正的程序。本书
第二部分的目的就是解决这个问题,带着你一步一步地开发出一个完整的程序。