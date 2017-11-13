

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

### Python web框架对比

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