from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_migrate import Migrate
import os

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


# 程序工厂创建函数，参数是使用的配置名称，配置从config字典中获取。
# 扩展对象通过,init_app()来初始化扩展。
def create_app():
    app = Flask(__name__)
    config_name = os.getenv('FLASKCONFIG') or 'default'
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    migrate.init_app(app=app, db=db)

    # 附加路由和自定义的错误页面
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


