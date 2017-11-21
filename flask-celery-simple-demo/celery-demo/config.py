# -*- coding: utf-8 -*-

from datetime import timedelta
from kombu import Queue

# 在任务调度中使用 msgpack 序列化，在任务结果中使用 json 序列化

BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

CELERY_TIMEZONE = 'Asia/Shanghai'
# CELERYBEAT_SCHEDULE = {
#     'send-every-30-seconds': {
#         'task': 'server.sendmail',
#         # 'schedule': crontab(hour=16, minute=30),
#         'schedule': timedelta(seconds=30),
#         'args': (dict(to='sparsematrix@163.com'),)
#     }
# }
#
# CELERY_QUEUES = (
#     Queue('default', routing_key='task.#'),
#     Queue('web_tasks', routing_key='web.#'),
# )
