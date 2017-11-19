#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

from flask import Blueprint

data = Blueprint('data', __name__,
                 # template_folder='/opt/auras/templates/',   #指定模板路径
                 # static_folder='/opt/auras/flask_bootstrap/static/',#指定静态文件路径
                 )

from service.application.controllers.data import views
