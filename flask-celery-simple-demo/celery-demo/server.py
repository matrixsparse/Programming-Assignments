# -*- coding:utf-8 -*-

import time
from app import celery
from celery.utils.log import get_task_logger

# 记录日志和重试
logger = get_task_logger(__name__)


@celery.task
def sendmail(mail):
    print('sending mail to %s ...' % mail['to'])
    time.sleep(2)
    print('mail send.')
    return 'Send Successful!'


# 装饰器app.task实际上是将一个正常的函数修饰成了一个 celery task 对象
@celery.task()  # 普通函数装饰为 celery task
def add(x, y, queue='default'):
    logger.info('token:{}:{}'.format(x, y))
    logger.info('Executing server args: {}'
                'args: {}'.format(x, y))
    return x + y
