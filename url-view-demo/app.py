from flask import Flask,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/list/')
def article_list():
    return "article list!"

@app.route('/article/<int:article_id>/')
def article_info(article_id):
    return "您请求的文章是:{}".format(article_id)


@app.route('/<any(blog,p):url_path>/<id>/')
def detail(url_path,id):
    if url_path == 'blog':
        return "您访问的是blog的详情id={}".format(id)
    else:
        return "您访问的是帖子的详情id={}".format(id)

# 通过?xxx=xxx形式传参
@app.route('/d/')
def d():
    wd = request.args.get('wd')
    return "您通过字符串传参为wd={}".format(wd)


if __name__ == '__main__':
    app.run()
