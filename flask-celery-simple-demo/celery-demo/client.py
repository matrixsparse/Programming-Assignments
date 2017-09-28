# -*- coding: utf-8 -*-

import time
from server import sendmail, add

# 调用任务会返回一个 AsyncResult 实例，可用于检查任务的状态，等待任务完成或获取返回值
# ready() 方法查看任务是否完成处理
result = add.delay(4, 4)  # 不要直接 add(4, 4)，这里需要用 celery 提供的接口 delay 进行调用
while not result.ready():
    time.sleep(1)
# print(result.backend)
print('task done: {0}'.format(result.get()))

answer = sendmail.delay({'to': "sparsematrix@163.com"})
# while not answer.ready():
#     time.sleep(1)
# print('task done: {0}'.format(answer.get()))

while 1:
    print('wait for ready')
    if answer.ready():
        break
    time.sleep(0.5)
print(answer.get())
