#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import json
from flask import render_template

from service.application.controllers.ranklist import ranklist
from service.application.utils.all_theme_link import get_novel_category_info


@ranklist.route('/', methods=['GET', 'POST'])  # 指定路由为/，因为run.py中指定了前缀，浏览器访问时，路径为http://IP/asset/
def index():
    # result = get_novel_category_info().get('result', '')
    return render_template('ranklist/ranklist.html')  # 返回index.html模板，路径默认在templates下


@ranklist.route('/handle', methods=['GET', 'POST'])  # 指定路由为/，因为run.py中指定了前缀，浏览器访问时，路径为http://IP/asset/handle
def handle():
    result = get_novel_category_info().get('result', '')
    return json.dumps({'code': 0, 'result': result})
