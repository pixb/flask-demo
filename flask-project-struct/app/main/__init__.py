# 创建蓝本
from flask import Blueprint

main = Blueprint('main',__name__)

# 在末尾导入，避免循环导入依赖
from . import views,error