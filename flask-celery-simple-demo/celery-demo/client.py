# -*- coding: utf-8 -*-

import time
from server import add
from celery import group, chain
from celery.schedules import crontab
from celery.task import periodic_task


# @periodic_task(run_every=crontab(hour='16', minute='58'))
# def schedule_sendmail():
#     print('sending mail task')
#     time.sleep(2)
#     print('mail send.')
#     return 'Send Successful！'


if __name__ == "__main__":
    result = add.apply_async(('sssssaaa', 'sdasda'), routing_key='task.add')
    # result = add.apply_async(args=(3, 2), queue='default')
    #
    # res = group(add.s(i, i) for i in range(10))()
    # res.get()
    #
    # res = chain(add.s(2, 2), add.s(4), add.s(8))()
    # res.get(timeout=1)
