# 基于Python Flask开发的自用框架

## 什么是蓝图？

```bash
一个应用中或跨应用组件和支持通用的模式
```

## 蓝图的作用？

* 将不同的功能模块化
* 构建大型应用
* 优化项目结构
* 增强可读性，易于维护

## 项目结构

```bash
tree
.
├── library # 公共配置文件存放目录
│   └── config
│       └── development.py
├── logs # 日志文件存放目录
│   └── service_.2017-11-02.log
├── manage.py # 主运行文件
├── README.md # 项目介绍文件
├── service
│   └── application
│       ├── controllers
│       │   ├── data # 数据功能目录
│       │   │   ├── __init__.py
│       │   │   └── views.py # 数据视图配置文件
│       │   ├── main.py # main功能目录
│       │   └── spider # spider功能目录
│       │       ├── __init__.py
│       │       └── views.py # spider视图配置文件
│       └── __init__.py
├── static
│   └── README.md
└── templates # 静态页面存放目录
    ├── data # data模块页面存放目录
    │   └── index.html
    ├── index.html # 首页
    └── spider # spider模块页面存放目录
        └── index.html
```

## Flask+uWSGI+nginx

```bash
使用的代理一共有两个，nginx和uwsgi，使用nginx的目的是为了安全和负载均衡

配置了nginx做前端代理
uwsgi作后端代理的服务器

在处理来自Internet的请求时，要先经过nginx的处理，nginx把请求再交给uwsgi，经过uwsgi才能访问到项目本身

没有nginx而只有uwsgi的服务器，则是Internet请求直接由uwsgi处理，并反馈到我们的项目中。
nginx可以实现安全过滤，防DDOS等保护安全的操作，并且如果配置了多台服务器，nginx可以保证服务器的负载相对均衡

而uwsgi则是一个web服务器，实现了WSGI协议(Web Server Gateway Interface)，http协议等，它可以接收和处理请求，发出响应等
```

### Nginx安装

* Mainline version：开发版
* Stable version：稳定版

```bash
[root@sparsematrix ~]# vim /etc/yum.repos.d/nginx.repo
```

```bash
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fimesan0trj21v40rmagh.jpg)

>查看yum源中nginx相关版本

```bash
[root@sparsematrix ~]# yum list | grep nginx
```

>使用yum源安装Nginx

```bash
[root@sparsematrix ~]# yum install nginx -y
```

>查看当前安装nginx版本

```bash
[root@sparsematrix ~]# nginx -v
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fimej0moqkj21bo02sjsj.jpg)

>查看Nginx编译参数

```bash
[root@sparsematrix ~]# nginx -V
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fimekxcei6j21da0w27tc.jpg)

>启动nginx

```bash
[root@sparsematrix ~]# /usr/sbin/nginx
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fiqzqmftanj22140ewgou.jpg)

>关闭nginx

```bash
[root@sparsematrix ~]# nginx -s stop
```

>平滑启动 nginx

```bash
nginx -s reload
```

### 安装uWSGI

```bash
在安装uWSGI前，需要解决 uWSGI 的依赖问题，因为uWSGI是一个C语言写的应用，所以我们需要C编译器，以及python开发相关组件：
```

```bash
[root@sparsematrix ~]# /usr/local/python3/bin/pip install uwsgi
```

>在项目根目录下创建一个配置文件runapp.ini(uwsgi支持多种配置文件格式，xml，ini，json等)

```bash
[root@sparsematrix flask-blueprint]# vi runapp.ini
```

```bash
[uwsgi]
; 启动程序时所使用的地址和端口，通常在本地运行flask项目，
; 地址和端口是127.0.0.1:5000,
; 不过在服务器上是通过uwsgi设置端口，通过uwsgi来启动项目，
; 也就是说启动了uwsgi，也就启动了项目。
; socket = 0.0.0.0:8000
; socket file's location
; socket 指定的是与 nginx 进行通信的端口文件
socket = /data/python_server/code/flask-blueprint/run/%n.sock
; 项目目录
chdir = /data/python_server/code/flask-blueprint
; flask程序的启动文件，通常在本地是通过运行python manage.py runserver 来启动项目的
wsgi-file = manage.py
; 程序内启用的application变量名
callable = app
; 处理器个数
processes = 4
; 线程个数
threads = 2
; 获取uwsgi统计信息的服务地址
stats = 127.0.0.1:9191
#permissions for the socket file
chmod-socket = 666
#the variable that holds a flask application inside the module imported at line #6
callable = app
#location of log files
logto = /data/python_server/code/flask-blueprint/run/%n.log
```

>启动uwsgi

```bash
uwsgi --ini runapp.ini &
```

### 使用nginx承担flask的web服务

>修改nginx的默认配置文件

```bash
vim /etc/nginx/conf.d/default.conf
```

```bash
server {
    listen       8088;
    server_name  localhost;

    access_log /data/nginx/logs/service_access.log main;
    error_log /data/nginx/logs/service_error.log;


    location /mystatus {
        stub_status;
    }

    location / {
    	include uwsgi_params;
    	uwsgi_pass unix:///data/python_server/code/flask-blueprint/run/runapp.sock; #  Nginx与uwsgi的交流方式
    }
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

>平滑启动 nginx

```bash
nginx -s reload
```

## 安装flask-sqlalchemy

```bash
pip install flask-sqlalchemy flask-script pymysql
```

## 定义模型，创建数据库表

>vim service/application/__init__.py

```bash
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/spider"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
```

```bash
db = SQLAlchemy(app)
```

>vim service/application/models/User.py

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

from flask_script import Manager
from service.application import db
from service.application import app


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


manager = Manager(app)

if __name__ == "__main__":
    # 将模型导入数据表
    db.create_all()
```

>手动指定User.py文件

```bash
可以在服务器数据库中发现，数据表成功生成！
```

### sqlalchemy操作命令

>创建表

```bash
db.create_all()
```

>删除表

```bash
db.drop_all()
```

>插入数据

```bash
u = User(username='',password='')
db.session.add(u)
db.session.commit()
```

>查询数据

* filter_by查询(精确查询)

```bash
u = User.query.filter_by(username='').first()
```

* get(主键):(id一般为主键)

```bash
User.query.get(1)
```

* filter查询(模糊查询)

```bash
User.query.filter(User.username.endswith('t')).all()
```

* 逻辑非查询

```bash
user = User.query.filter(User.username != '' ).first()
```

or

```bash
from sqlalchemy import not_
user = User.query.filter(not_(User.username == '' )).first()
```

* 逻辑与

```bash
from sqlalchemy import and_
user = User.query.filter(and_(User.username =='',User.email.endswith(''))).first()
```

* 逻辑或

```bash
from sqlalchemy import or_
user = User.query.filter(or_(User.username !='',User.email.endswith(''))).first()
```

* first()返回查询到的第一个对象

```bash
user = User.query.first()
```

* all()返回查询到的所有对象

```bash
user = User.query.all()
```

>删除数据

```bash
user = User.query.first()
db.session.delete(user)
db.session.commit()
User.query.all()
```

>更新数据

```bash
user = User.query.first()
user.username = ''
db.sesssion.commit()
User.query.first()
```


