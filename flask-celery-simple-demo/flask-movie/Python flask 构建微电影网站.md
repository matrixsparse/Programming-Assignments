
## 项目结构图

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fi6x569m1bj21h014gafq.jpg)

### 前台

* 数据模型：model.py
* 表单处理：home/forms.py
* 模板目录：templates/home
* 静态目录：static

### 后台

* 数据模型：model.py
* 表单处理：admin/forms.py
* 模板目录：templates/admin
* 静态目录：static

### 前后台项目目录

* manage.py # 入口启动脚本
* app # 项目app
    * __init__.py # 初始化文件
    * models.py # 数据模型文件
    * static # 静态目录
    * home # 前台模块
        * __init__.py # 初始化脚本
        * views.py # 视图处理文件
        * forms.py # 表单处理文件
    * admin # 后台模块
        * __init__.py # 初始化脚本
        * views.py # 视图处理文件
        * forms.py # 表单处理文件
    * templates # 模板目录
        * home/admin # 前台/后台模板

## 开发及生产环境

* centos7
* python3
* mysql
* html5
* flask
* nginx

## Python Flask

### 国内使用Python开发Web的公司

* 果壳：Flask
* 知乎：Tornado
* 豆瓣：Quixote

### Python web框架对比

| Flask | Django | Tornado |
| :------: | :------: | :------: |
| Flask拓展丰富，亢余度小，可自由选择组合各种插件，性能优越，相比其他web框架十分轻量级，其优雅的设计哲学易于学习掌握，小型项目快速开发，大型项目毫无压力。Flask灵活开发，Python高手基本都会喜欢Flask。 | Django是重量级全栈型web框架，虽然功能其强大，但亢余度高，自带ORM和模板引擎，灵活和自动度不够高，开发小型项目时显得过于臃肿与庞大 | Tornado是一个强大的、支持协程、高效并发且可拓展的Web服务器，发布于2009年9月，应用于FriendFeed、Facebook等社交网站，Tornado的强项在于可以利用它的异步协程机制开发高并发的服务器系统 |


### Flask简介

* 轻量级Web应用框架
* WSGI工具箱采用Werkzeug
* 模板引擎则使用Jinja2
* Flask使用BSD授权

### 安装虚拟环境

```bash
sparsematrix:~ matrix$ sudo pip3 install virtualenv
```

## Virtualenv的使用及flask的安装

### virtualenv的使用

>创建虚拟环境

```bash
sparsematrix:Desktop matrix$ virtualenv venv
New python executable in /Users/matrix/Desktop/venv/bin/python
Installing setuptools, pip, wheel...done.
```

>激活虚拟环境

```bash
sparsematrix:Desktop matrix$ source venv/bin/activate
(venv) sparsematrix:Desktop matrix$ pip3 freeze
```

>退出虚拟环境

```bash
deactivate
```

### Flask的安装

>安装前检测

```bash
pip3 freeze
```

>安装flask

```bash
(venv) sparsematrix:Desktop matrix$ pip3 install -i http://pypi.douban.com/simple/ flask
```

>安装后检测

```bash
pip3 freeze
```

### Flask Hello World！

```bash
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world!"

if __name__ == "__main__":
    app.run()
```

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fi7dk3wopgj21mo09gwgb.jpg)

## 蓝图构建项目目录

### 什么是蓝图

```bash
一个应用中或跨应用制作应用软件和支持通用的模式
```

### 蓝图的作用

* 将不同的功能模块化
* 构建大型应用
* 优化项目结构
* 增强可读性，易于维护

### 蓝图构建项目目录

>定义蓝图(app/admin/__init__.py)

```bash
# -*- coding: utf-8 -*-
# 初始化文件

from flask import Blueprint

admin = Blueprint("admin",__name__)

import app.admin.views
```

>定义蓝图(app/home/__init__.py)

```bash
# -*- coding: utf-8 -*-
# 初始化文件

from flask import Blueprint

home = Blueprint("home",__name__)

import app.home.views
```

>注册蓝图(app/__init__.py)

```bash
# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

app.debug = True

# 导入蓝图对象
from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint


# 注册蓝图
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix = "/admin")
```

>视图文件(app/home/views.py)

```bash
# -*- coding: utf-8 -*-
# 视图文件

from . import home

@home.route("/")
def index():
    return "<h1 style='color:#369'>this is home</h1>"
```

>视图文件(app/admin/views.py)

```bash
# -*- coding: utf-8 -*-
# 视图文件

from . import admin

@admin.route("/")
def index():
    return "<h1 style='color:#666'>this is home</h1>"
```

>入口文件(manage.py)

```bash
# -*- coding: utf-8 -*-
# 入口文件

from app import app

if __name__ == "__main__":
    app.run()
```

## 会员及会员登录日志数据模型设计

### 安装数据库连接依赖包

```bash
sparsematrix:~ matrix$ sudo pip3 install flask-sqlalchemy
```

>连接mysql数据库

```bash
sparsematrix:~ matrix$ mysql -uroot -p123456
```

>查看数据库信息

```bash
mysql> \s
```

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fi8nbkl89qj21d80xi7i7.jpg)

>创建数据库

```bash
mysql> create database Movie;
```

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fi8nbkagrnj21da04g0ug.jpg)



### 定义mysql数据库连接

### 定义会员数据模型

>models.py

```bash
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:8889/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


# 会员
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码
    email = db.Column(db.String(100), unique=True)  # 邮箱
    phone = db.Column(db.String(11), unique=True)  # 手机号码
    info = db.Column(db.Text)  # 个性简介
    face = db.Column(db.String(255), unique=True)  # 头像
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 注册时间
    uuid = db.Column(db.String(255))  # 唯一标志符
    userlogs = db.relationship('Userlog', backref='user')  # 会员日志外键关系关联
    comments = db.relationship('Comment', backref='user')  # 评论外键关联
    moviecols = db.relationship('Moviecol', backref='user')  # 电影收藏外键关系关联

    def __repr__(self):
        return "<User %r>" % self.name


# 会员登录日志
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属会员
    ip = db.Column(db.String(100))  # 登录
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 最近登录时间

    def __repr__(self):
        return "<Userlog %r>" % self.id


# 标签
class Tag(db.Model):
    __tablename = "tag"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 标题
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    movie = db.relationship("Movie", backref="tag")  # 电影外键关系关联

    def __repr__(self):
        return "<Tag %r>" % self.name


# 电影
class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    url = db.Column(db.String(255), unique=True)  # 地址
    info = db.Column(db.Text)  # 简介
    logo = db.Column(db.String(255), unique=True)  # 封面
    star = db.Column(db.SmallInteger)  # 星级
    playnum = db.Column(db.BigInteger)  # 播放量
    commentnum = db.Column(db.BigInteger)  # 评论量
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 所属标签
    area = db.Column(db.String(255))  # 上映地区
    release_time = db.Column(db.String(255))  # 上映时间
    length = db.Column(db.String(100))  # 播放时间
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    comments = db.relationship("Comment", backref="movie")  # 评论外键关系关联
    moviecols = db.relationship('Moviecol', backref="movie")  # 电影收藏外键关系关联

    def __repr__(self):
        return "<Movie %r>" % self.title


# 上映预告
class Preview(db.Model):
    __tablename__ = "preview"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(255), unique=True)  # 标题
    logo = db.Column(db.String(255), unique=True)  # 封面
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<Preview %r>" % self.title


# 评论
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 编号
    content = db.Column(db.Text)  # 内容
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加评论

    def __repr__(self):
        return "<Comment %r>" % self.id


# 电影收藏
class Moviecol(db.Model):
    __tablename__ = "moviecol"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    content = db.Column(db.Text)  # 内容
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 所属电影
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # 所属用户
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<Moviecol %r>" % self.id


# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    url = db.Column(db.String(255), unique=True)  # 唯一地址
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    auths = db.Column(db.String(200))  # 权限
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    admin = db.relationship("Admin", backref="role")  # 管理员外键关系关联

    def __repr__(self):
        return "<Role %r>" % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)  # 名称
    pwd = db.Column(db.String(100))  # 密码
    is_super = db.Column(db.SmallInteger)  # 是否是超级管理员，0为超级管理员
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))  # 所属角色
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间
    adminlogs = db.relationship("Adminlog", backref="admin")  # 管理员登录日志外键关联
    oplogs = db.relationship("Oplog", backref="admin")  # 管理员操作日志外键关联

    def __repr__(self):
        return "<Admin %r>" % self.name


# 管理员登录日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录IP
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 登录时间

    def __repr__(self):
        return "<Adminlog %r>" % self.id


# 操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 所属管理员
    ip = db.Column(db.String(100))  # 登录IP
    reason = db.Column(db.String(100))  # 原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # 添加时间

    def __repr__(self):
        return "<Oplog %r>" % self.id


if __name__ == "__main__":
    # 将模型导入数据表
    # db.create_all()
    # 插入数据
    role = Role(
        name="超级管理员",
        auths=""
    )
    db.session.add(role)
    db.session.commit()
```

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fi9u7m63i7j21d60c8wmc.jpg)

>进入数据库查看表是否创建成功

```bash
mysql> use Movie;
```

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fi9udhnljhj21d802odgp.jpg)

```bash
mysql> show tables;
```

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fi9udhsvzjj21dg0pe7b2.jpg)

```bash
mysql> desc admin
```

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fi9ulfahrdj21d60h6tge.jpg)

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fif752833xj21d20a2q6c.jpg)


SET character_set_server=utf8,character_set_connection=utf8, character_set_results=utf8, character_set_client=utf8;

mysql> flush privileges;

## 前台布局搭建

### 静态文件引入

```bash
{{url_for('static',filename='文件路径')]}}
```

### 定义路由

```bash
{{url_for('模块名.视图名',变量=参数)}}
```

### 定义数据块

```bash
{% block 数据块名称 %}...{% endblock %}
```

```bash
sparsematrix:~ matrix$ sudo pip3 install flask_wtf
```

### 生成唯一标识

```
sparsematrix:~ matrix$ python3
Python 3.6.1 (default, Apr  4 2017, 09:40:21)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import uuid
>>> uuid.uuid4().hex
'6b1193db99e042508923b35a0358460f'
```

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fiql27wgjkj21m409s0yr.jpg)
