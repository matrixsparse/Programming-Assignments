#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import traceback
from flask import jsonify
from library.config.error import Err
from service.application.utils.spider import Spider


def get_chapter_data(**kwargs):
    s = Spider()
    result = s.get_chapter_data()
    data = '{}'.format(result)
    return {'code': 0, 'data': data}


def get_content_data(title=None, chapter=None, **kwargs):
    try:
        if title is None and isinstance(title, str):
            return {'code': Err.Invalid_params, 'data': Err.Msg.Invalid_params}
        elif chapter is None and isinstance(chapter, str):
            return {'code': Err.Invalid_params, 'data': Err.Msg.Invalid_params}
    except:
        print(traceback.format_exc())
        return {'code': Err.Invalid_params, 'data': Err.Msg.Invalid_params}
    s = Spider()
    result = s.get_content_data(title, chapter)
    data = '{}'.format(result)
    return {'code': 0, 'data': data}
