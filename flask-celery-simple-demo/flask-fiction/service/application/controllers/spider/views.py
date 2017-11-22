#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import json
from flask import render_template
from service.application.controllers.spider import spider


@spider.route('/', methods=['GET', 'POST'])
def index():
    return render_template('spider/index.html')


@spider.route('/handle', methods=['GET', 'POST'])
def handle():
    return json.dumps({'code': 0, 'data': 'success'})

# @spider.route('/get_chapter_data', methods=['GET', 'POST'])
# def get_chapter_data():
#     s = Spider()
#     result = s.get_chapter_data()
#     return "{'code': 0, 'data': '%s'}" % (result)
#
#
# @spider.route('/get_content_data', methods=['GET', 'POST'])
# def get_content_data():
#     args = dict(request.args.items())
#     print(args)
#     title = args.get('title')
#     chapter = args.get('chapter')
#     try:
#         if not args.has_key('title') and isinstance(title, str):
#             return {'code': Err.Invalid_params, 'data': Err.Msg.Invalid_params}
#         elif not args.has_key('chapter') is None and isinstance(chapter, str):
#             return {'code': Err.Invalid_params, 'data': Err.Msg.Invalid_params}
#     except:
#         print(traceback.format_exc())
#         return {'code': Err.Invalid_params, 'data': Err.Msg.Invalid_params}
#     s = Spider()
#     result = s.get_content_data(title, chapter)
#     return "{'code': 0, 'data': '%s'}" % (result)
