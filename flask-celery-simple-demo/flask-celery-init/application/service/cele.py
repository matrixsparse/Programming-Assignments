# -*- coding: utf-8 -*-

import celery
from celery.schedules import crontab

app = celery.Celery('cele', broker='redis://localhost:6379/0')

# @app.task
# def send(message):
#     return message


app.conf.beat_schedule = {
    'send-every-60-seconds': {
        'task': 'cele.send',
        # 每两小时执行一次
        # 'schedule': 3600.0,

        # 每十五分钟执行一次
        'schedule': crontab(minute='*/1'),
        # 每两小时执行一次
        # 'schedule': crontab(hour='*/1.8'),
        'args': ('This is my fuck world！',)
    },
}
