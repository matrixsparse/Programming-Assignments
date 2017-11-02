from flask import render_template
from asset import asset


@asset.route('/')  # 指定路由为/，因为run.py中指定了前缀，浏览器访问时，路径为http://IP/asset/
def index():
    print('__name__', __name__)
    return render_template('asset/index.html')  # 返回index.html模板，路径默认在templates下
