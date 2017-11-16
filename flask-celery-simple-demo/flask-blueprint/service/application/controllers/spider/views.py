#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import traceback
from flask import request
from flask import render_template
from library.config.error import Err
from service.application.service.spider import Spider
from service.application.controllers.spider import spider


@spider.route('/', methods=['GET', 'POST'])
def index():
    print('__name__', __name__)
    return render_template('spider/index.html')


@spider.route('/handle', methods=['GET', 'POST'])
def handle():
    print('编写逻辑')
    return "{'code': 0, 'msg': 'success'}"


@spider.route('/get_chatper_list', methods=['GET', 'POST'])
def get_chatper_list():
    s = Spider()
    result = s.get_chapter_data()
    return "{'code': 0, 'data': '%s'}" % (result)


@spider.route('/get_content_list', methods=['GET', 'POST'])
def get_content_data():
    args = dict(request.args.items())
    print(args)
    title = args.get('title')
    chapter = args.get('chapter')
    try:
        if not args.has_key('title') and isinstance(title, str):
            return {'code': Err.Invalid_params, 'data': Err.Msg.Invalid_params}
        elif not args.has_key('chapter') is None and isinstance(chapter, str):
            return {'code': Err.Invalid_params, 'data': Err.Msg.Invalid_params}
    except:
        print(traceback.format_exc())
        return {'code': Err.Invalid_params, 'data': Err.Msg.Invalid_params}
    s = Spider()
    result = s.get_content_data(title, chapter)
    return "{'code': 0, 'data': '%s'}" % (result)
