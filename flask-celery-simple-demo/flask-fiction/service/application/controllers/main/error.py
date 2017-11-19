#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import json
import traceback
from flask import request, jsonify, g
from service.application.__init__ import app
from library.config.error import Err
from service.application.controllers.main import main


@main.app_errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return json.dumps({'code': Err.Not_found, 'msg': Err.Msg.Not_found}), 404


@main.app_errorhandler(500)
def nterror(error):
    try:
        args = request.args if request.method == 'GET' else request.form
        app.logger.debug(args)
    except:
        app.logger.error(traceback.format_exc())
        app.logger.error(error)
    return json.dumps({'code': Err.Unknown_error, 'msg': Err.Msg.Unknown_error}), 500
