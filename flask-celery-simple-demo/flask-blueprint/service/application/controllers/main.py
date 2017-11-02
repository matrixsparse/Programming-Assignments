#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix
import traceback
# from service.application.__init__ import app
from flask import Blueprint
from flask import request, jsonify, g
from . import main

main = Blueprint('main', __name__,
                 # template_folder='/opt/auras/templates/',   #指定模板路径
                 # static_folder='/opt/auras/flask_bootstrap/static/',#指定静态文件路径
                 )


@main.route('/sssss')
def main_before_request():
    try:
        if request.url_rule.rule.startswith('/service/'):
            args = dict(request.args.items())
            # if args.get('token') not in app.config['AUTH_TOKEN']:
            #     print(args, app.config['AUTH_TOKEN'])
    except:
        pass
        # app.logger.error(traceback.print_exc())


if __name__ == "__main__":
    # print(__name__)
    print('测试')
