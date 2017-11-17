#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import time
import traceback
from flask import request, jsonify, g
from service.application.__init__ import app
from library.config.error import Err
from service.application.controllers.main import main


@main.before_request
def main_before_request():
    try:
        if request.url_rule.rule.startswith('/service/'):
            args = dict(request.args.items())
            print('args：', args)
            if args.get('token') not in app.config['AUTH_TOKEN']:
                return jsonify({'code': Err.Invalid_token, 'msg': Err.Msg.Invalid_token})
    except:
        app.logger.error(traceback.format_exc())
        return jsonify({'code': Err.Internal_server_error, 'msg': Err.Msg.Internal_server_error})


@main.route('/', methods=['GET', 'POST'])
def index():
    print('__name__', __name__)
    return 'success'


@main.route('/service/<module_name>/<func_name>', methods=['GET', 'POST'])
def service(module_name, func_name):
    try:
        if module_name.startswith('_') or func_name.startswith('_'):
            return jsonify({'code': Err.Forbidden, 'msg': Err.Msg.Forbidden})
        data = dict(request.args.items())
        print('data：', data)
        print('module_name：', module_name)
        print('func_name：', func_name)
        print('globals().get(module_name, object)：', globals().get(module_name, object))
        func = getattr(globals().get(module_name, object), func_name, None)
        print('func：', func)

        if not callable(func):
            return jsonify({'code': Err.Not_found, 'msg': Err.Msg.Not_found})
        if request.method == 'GET':
            data = dict(request.args.items())
        else:
            data = request.get_json()
            data = data if isinstance(data, dict) else {}

        print('data：%s' % data)
        g.ip = request.remote_addr
        app.logger.debug('g.ip：%s' % g.ip)
        start = time.time()
        # 执行函数
        result = func(**data)
        print('result：', result)
        end = time.time()
        app.logger.debug('run %s.%s cost %.6f s...' % (module_name, func_name, (end - start)))
        if isinstance(result, str):
            if result.find('callback=') != -1:
                return result.split('callback=')[1]
        else:
            return jsonify(result)
    except:
        app.logger.error(traceback.format_exc())
        return jsonify({'code': Err.Internal_server_error, 'msg': Err.Msg.Internal_server_error})


@main.route('/service/<func_name>', methods=['GET', 'POST'])
def old_service(func_name):
    try:
        print('func_name：', func_name)
        module_name = 'spider'
        func = getattr(globals().get(module_name, object), func_name, None)
        if not callable(func):
            return jsonify({'code': Err.Not_found, 'msg': Err.Msg.Not_found})

        data = request.get_json()
        data = data if isinstance(data, dict) else {}
        g.ip = request.remote_addr
        start = time.time()
        # 执行函数
        result = func(**data)
        end = time.time()
        app.logger.debug('run %s.%s cost %.6f s...' % (module_name, func_name, (end - start)))
        return jsonify(result)
    except:
        app.logger.error(traceback.format_exc())
        return jsonify({'code': Err.Internal_server_error, 'msg': Err.Msg.Internal_server_error})
