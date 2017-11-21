# -*- coding: utf-8 -*-

# 主函数分离

from celery import Celery

celery = Celery('app', include=['server'])
celery.config_from_object('config')
