#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask import render_template

from service.application.controllers.data import data
from service.application.controllers.spider import spider


def create_app():
    app = Flask(__name__,
                template_folder='templates',  # 指定模板路径，可以是相对路径，也可以是绝对路径
                static_folder='static'  # 指定静态文件前缀，默认静态文件路径同前缀
                )

    app.register_blueprint(spider, url_prefix='/spider')  # 注册spider蓝图，并指定前缀
    app.register_blueprint(data, url_prefix='/data')  # 注册data蓝图，并指定前缀

    lOG_PATH = 'logs/%s' % 'service_'
    filehandler = TimedRotatingFileHandler(
        filename=lOG_PATH,
        when="D",
        interval=1,
        # 保留日志个数,默认的0是不会自动删除掉日志
        backupCount=0,
        encoding='utf-8'
    )

    datefmt_str = '%Y-%m-%d %H:%M:%S'
    format_str = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s'
    formatter = logging.Formatter(format_str, datefmt_str)
    # 设置后缀名称
    filehandler.suffix = "%Y-%m-%d_%H-%M.log"
    filehandler.setFormatter(formatter)
    filehandler.setLevel(logging.DEBUG)
    app.logger.addHandler(filehandler)

    return app


app = create_app()


@app.route('/')
def hello_world():
    # return "<h1>Hello World！</h1>"
    app.logger.debug('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)  # 运行flask http程序，host指定监听IP，port指定监听端口，调试时需要开启debug模式
