# -*- coding: utf-8 -*-

# 主函数分离

from celery import Celery

app = Celery('app', include=['server'])
app.config_from_object('config')
