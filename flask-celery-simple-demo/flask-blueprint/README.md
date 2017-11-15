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

>修改nginx默认配置文件

* 阿里云服务器要在安全组中设置安全组规则
* 使用非80端口时，检查防火墙是否关闭

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
        #设置主机头和客户端真实地址，以便服务器获取客户端真实IP
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_buffering off;
	include uwsgi_params;
	uwsgi_pass unix:///data/python_server/code/flask-blueprint/run/runapp.sock;
	#root   /usr/share/nginx/html;
        #index  index.html index.htm;
    }

    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }
}
```

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
[root@sparsematrix ~]# pip3 install uwsgi
```

>在项目根目录下创建一个配置文件config.ini(uwsgi支持多种配置文件格式，xml，ini，json等)

```bash
[root@sparsematrix flask-blueprint]# vi config.ini
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
socket = /data/python_server/code/flask-blueprint/run/runapp.sock
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
logto = /data/python_server/code/flask-blueprint/run/runapp.log
```

>启动uwsgi

```bash
uwsgi --ini config.ini &
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

## 使用Supervisor管理uwsgi进程[Supervisor只支持python2.x]

```bash
Supervisor是基于Python的进程管理工具，可以更简单的监听、启停、重启服务器上的一个或多个后台进程，是Linux服务器管理的高效工具

Supervisor管理的进程，当一个进程意外被杀死，supervisort监听到进程挂掉后，会自动将它重新拉起
其进程自动恢复的功能，不再需要自己写shell脚本来控制
```

>Supervisor 有两个主要的组成部分：

* supervisord，运行Supervisor时会启动一个进程supervisord，它负责启动所管理的进程，并将所管理的进程作为自己的子进程来启动，而且可以在所管理的进程出现崩溃时自动重启

* supervisorctl，是命令行管理工具，可以用来执行stop、start、restart等命令，来对这些子进程进行管理

### 安装supervisor

```bash
su matrix
```

```bash
workon pyenv2.7
```

```bash
easy_install supervisor
```

### 测试是否安装成功

```bash
echo_supervisord_conf
```

### 创建目录&配置文件

>创建文件夹

```bash
mkdir -p /etc/supervisord.d
mkdir -p /etc/supervisord.d/config
chown -R matrix:matrix /etc/supervisord.d
```

>创建日志目录

```bash
mkdir -p /var/log/supervisor/
chown -R matrix:matrix /var/log/supervisor/
```

```bash
echo_supervisord_conf > /etc/supervisord.d/supervisord.conf
```

>如果出现没有权限的问题，可以使用这条命令

```bash
sudo su - root -c "echo_supervisord_conf > /etc/supervisord.d/supervisord.conf"
```

> supervisor安装完成后会生成三个执行程序：
* supervisortd【supervisor的守护进程服务（用于接收进程管理命令）】
* supervisorctl【客户端（用于和守护进程通信，发送管理进程的指令）】
* echo_supervisord_conf【生成初始配置文件程序】


### 编辑/etc/supervisord.d/supervisord.conf文件

```bash
vim /etc/supervisord.d/supervisord.conf
```

```bash
[unix_http_server]
; 修改为/etc/supervisord.d目录，避免被系统删除
file=/etc/supervisord.d/supervisor.sock   ; the path to the socket file
;chmod=0700                 ; socket file mode (default 0700)
;chown=nobody:nogroup       ; socket file uid:gid owner
;username=user              ; default is no username (open server)
;password=123               ; default is no password (open server)

;[inet_http_server]         ; inet (TCP) server disabled by default
;port=127.0.0.1:9001        ; ip_address:port specifier, *:port for all iface
;username=user              ; default is no username (open server)
;password=123               ; default is no password (open server)

[supervisord]
; logfile=/tmp/supervisord.log ; main log file; default $CWD/supervisord.log
; 修改为 /var/log 目录，避免被系统删除
logfile=/var/log/supervisor/supervisord.log ;
; 日志文件多大时进行分割
logfile_maxbytes=50MB        ; max main logfile bytes b4 rotation; default 50MB
; 最多保留多少份日志文件
logfile_backups=10           ; # of main logfile backups; 0 means none, default 10
loglevel=info                ; log level; default info; others: debug,warn,trace
; 修改为/etc/supervisord.d目录，避免被系统删除
pidfile=/etc/supervisord.d/supervisord.pid ; supervisord pidfile; default supervisord.pid
nodaemon=false               ; start in foreground if true; default false
minfds=1024                  ; min. avail startup file descriptors; default 1024
minprocs=200                 ; min. avail process descriptors;default 200
;umask=022                   ; process file creation umask; default 022
; 设置启动supervisord的用户，一般情况下不要轻易用root用户来启动，除非你真的确定要这么做
user=matrix                 ; default is current user, required if root

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
; 必须和'unix_http_server'里面的设定匹配
; 修改为/etc/supervisor目录，避免被系统删除
;serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL  for a unix socket
serverurl=unix:///etc/supervisord.d/supervisor.sock ;

[include]
files = /etc/supervisord.d/config/*.ini
```

### 编辑/etc/supervisord.d/config/uwsgi.ini

```bash
vim /etc/supervisord.d/config/uwsgi.ini
```

```bash
[group:uwsgi]
programs = uwsgi.app

[program:uwsgi.app]
; 启动命令，可以看出与手动在命令行启动的命令是一样的
command=/home/matrix/.virtualenvs/pyenv3.6/bin/uwsgi --ini /data/python_server/code/flask-blueprint/config.ini
numprocs=1
numprocs_start=0
priority=999
; 在supervisord启动的时候也自动启动
autostart=true
; 启动3秒后没有异常退出，就当作已经正常启动了
startsecs=3
; 启动失败自动重试次数，默认是3
startretries=3
exitcodes=0,2
stopsignal=QUIT
stopwaitsecs=60
directory=/data/python_server/code/flask-blueprint
user=matrix
; 默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
stopasgroup=false
; 默认为false，向进程组发送kill信号，包括子进程
killasgroup=false
redirect_stderr=true
;stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile=/var/log/supervisor/uwsgi.log
; 日志文件多大时进行分割
stdout_logfile_maxbytes=250MB
; 最多保留多少份日志文件
stdout_logfile_backups=10
stderr_logfile=/var/log/supervisor/uwsgi.err
stderr_logfile_maxbytes=250MB
stderr_logfile_backups=10
; 可以通过 environment 来添加需要的环境变量，一种常见的用法是修改 PYTHONPATH
environment=PYTHONPATH="/data/python_server/code/flask-blueprint"
```

### 启动supervisor

```bash
/home/matrix/.virtualenvs/pyenv2.7/bin/supervisord -c /etc/supervisord.d/supervisord.conf
```

### 查看supervisor是否启动成功

```bash
ps -ef | grep '/etc/supervisord.d/supervisord.conf'
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flilhrt4dbj20ys0203yl.jpg)

### 查看supervisord.log

```bash
tail -f /var/log/supervisor/supervisord.log
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flisb67a70j20z1072aaw.jpg)

## supervisorctl命令介绍

```bash
# 停止某一个进程，program_name 为 [program:x] 里的 x
supervisorctl stop program_name
# 启动某个进程
supervisorctl start program_name
# 重启某个进程
supervisorctl restart program_name
# 结束所有属于名为 groupworker 这个分组的进程 (start，restart 同理)
supervisorctl stop groupworker:
# 结束 groupworker:name1 这个进程 (start，restart 同理)
supervisorctl stop groupworker:name1
# 停止全部进程，注：start、restart、stop 都不会载入最新的配置文件
supervisorctl stop all
# 载入最新的配置文件，停止原有进程并按新的配置启动、管理所有进程
supervisorctl reload
# 根据最新的配置文件，启动新配置或有改动的进程，配置没有改动的进程不会受影响而重启
supervisorctl update
# 查看进程的状态
supervisorctl status
```

>查看进程状态

```bash
supervisorctl status
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flisb671okj20kk019t8l.jpg)

>重启进程

```bash
supervisorctl restart uwsgi:uwsgi.app
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fliseph4huj20of01wq2u.jpg)

## 查看supervisord所在路径

```bash
which supervisord
```

## 使用浏览器来管理

```bash
supervisor 同时提供了通过浏览器来管理进程的方法，只需要注释掉如下几行就可以了
```

```bash
;[inet_http_server]         ; inet (TCP) server disabled by default
;port=192.168.3.244:9001        ; (ip_address:port specifier, *:port for ;all iface)
;username=user              ; (default is no username (open server))
;password=123               ; (default is no password (open server))
[supervisorctl]
...
;serverurl=http://192.168.3.244:9001 ; use an http:// url to specify an inet socket
;username=chris              ; should be same as http_username if set
;password=123                ; should be same as http_password if set
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flajqtxissj20ot037glm.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flajqtbr0bj20qg06yaak.jpg)

>访问浏览器地址栏：http://192.168.3.244:9001/

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fl1lvrh2stj20ws07mt98.jpg)

## 开机自动启动Supervisord

```bash
Linux在启动的时候会执行/etc/rc.local里面的脚本，所以在这里添加执行命令就可以
```

```bash
vim /etc/rc.local
```

```bash
/home/matrix/.virtualenvs/pyenv2.7/bin/supervisord -c /etc/supervisord.d/supervisord.conf
```

### 启用rc.local服务

```bash
sudo systemctl enable rc-local.service
```

## Centos7安装MySql

### 下载mysql的repo源

```bash
wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
```

### 安装mysql-community-release-el7-5.noarch.rpm包

```bash
rpm -ivh mysql-community-release-el7-5.noarch.rpm
```

>安装这个包后，会获得两个mysql的yum repo源

```bash
/etc/yum.repos.d/mysql-community.repo
/etc/yum.repos.d/mysql-community-source.repo。
```

### 安装mysql

```bash
yum install mysql-server -y
```

### 重置密码

```bash
mysql -u root
```

>报错

```bash
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock'
```

>报错原因

```bash
/var/lib/mysql访问权限的问题，把/var/lib/mysql的拥有者改为当前用户即可
```

>解决

```bash
chown -R root:root /var/lib/mysql
```

>重启服务

```bash
service mysqld restart
```

>重置密码

```bash
mysql -u root
mysql > use mysql;
mysql > update user set password=password('123456') where user='root';
mysql > quit;
```

>重启服务

```bash
service mysqld restart
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


