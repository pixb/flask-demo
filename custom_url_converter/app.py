from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)
# 一个url中，含有手机号码的变量，必须限定这个变量的字符串格式满足手机号码的格式
class TelephoneConveter(BaseConverter):
    regex = r'1[34587]\d{9}'


# 添加列表转换器
class ListConverters(BaseConverter):
    # to_python可以将值返回给视图函数
    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        return '+'.join(value)

app.url_map.converters['tel'] = TelephoneConveter
app.url_map.converters['list'] = ListConverters


@app.route('/',methods=['GET','POST'])
def hello_world():
    return 'Hello World!'

@app.route('/user/<string:user_id>')
def user_profile(user_id):
    return '您输入的user_id为{}'.format(user_id)

@app.route('/telephone/<tel:my_tel>/')
def my_tel(my_tel):
    return 'Your telephone number is {}'.format(my_tel)

# 还是用list转换器，将参数转换为列表
@app.route('/posts/<list:boards>/')
def posts(boards):
    return "Your access board is {},url is {}".format(boards,url_for('posts',boards=boards))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')