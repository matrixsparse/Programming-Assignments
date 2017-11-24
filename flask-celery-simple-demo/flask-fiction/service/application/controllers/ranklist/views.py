#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import json
from flask import render_template, request

from service.application.controllers.ranklist import ranklist
from service.application.utils.all_theme_link import get_novel_category_info


@ranklist.route('/', methods=['GET', 'POST'])
def index():
    args = dict(request.args.items())
    print(args)
    return render_template('ranklist/ranklist.html')


@ranklist.route('/test', methods=['GET', 'POST'])
def test():
    args = dict(request.args.items())
    print(args)
    return render_template('ranklist/test.html')


@ranklist.route('/handle', methods=['GET', 'POST'])
def handle(skip_num=0, limit_num=10):
    args = dict(request.args.items())
    skip_num = int(args.get('skip_num', 0))
    result = get_novel_category_info(skip_num, limit_num).get('result', '')
    return json.dumps({'code': 0, 'result': result})
