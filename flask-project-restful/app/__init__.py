from config import config
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
import os

from .models import Base
from .api import video

db = SQLAlchemy(model_class=Base)  # noqa: F821
app = Flask(__name__)

CORS(app, supports_credentials=True)

app = Flask(__name__)
migrate = Migrate(app, db)
config_name = os.getenv("FLASK_CONFIG") or "default"  # noqa: F821
app.config.from_object(config[config_name])
config[config_name].init_app(app)
db.init_app(app)
migrate.init_app(app, db)
api = Api(app)

# add resource to api
api.add_resource(video.VideoList, "/api/videos")
api.add_resource(video.Video, "/api/videos/<int:video_id>")


# 程序工厂创建函数，参数是使用的配置名称，配置从config字典中获取。
# 扩展对象通过,init_app()来初始化扩展。
def create_app():
    # 支持跨域
    return app
