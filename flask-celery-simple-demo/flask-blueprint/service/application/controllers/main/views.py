#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import traceback
# from service.application.__init__ import app
from flask import request, jsonify, g

from service.application.controllers.main import main


@main.before_request
def main_before_request():
    try:
        print(request.url_rule.rule)
        if request.url_rule.rule.startswith('/service/'):
            args = dict(request.args.items())
            print('args', args)
            # if args.get('token') not in app.config['AUTH_TOKEN']:
            #     print(args, app.config['AUTH_TOKEN'])
    except:
        pass
        # app.logger.error(traceback.print_exc())


@main.route('/', methods=['GET', 'POST'])
def index():
    return 'success'


if __name__ == "__main__":
    print(app.config['AUTH_TOKEN'])
