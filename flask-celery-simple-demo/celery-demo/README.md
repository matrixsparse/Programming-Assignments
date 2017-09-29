# 分布式队列神器Celery

## Celery是什么?

```bash
Celery 是一个由 Python 编写的简单、灵活、可靠的用来处理大量信息的分布式系统,它同时提供`操作`和`维护`分布式系统所需的工具
Celery 专注于`实时`任务处理，支持`任务调度`
Celery 是一个分布式队列的管理工具，用 Celery 提供的接口可以快速实现并管理一个`分布式的任务队列`
```

## Celery架构

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjzfp0bhfaj20i60ghdg4.jpg)

## Celery基本概念

```bash
(本文以 Celery4.0 为基础进行书写)
Celery 本身不是任务队列，它是管理分布式任务队列的工具，或者换一种说法，它封装好了操作常见任务队列的各种操作，我们用它可以快速进行任务队列的使用与管理，当然你也可以自己看 rabbitmq 等队列的文档然后自己实现相关操作都是没有问题的
Celery 是语言无关的，虽然它是用 Python 实现的，但他提供了其他常见语言的接口支持
只是如果你恰好使用 Python 进行开发那么使用 Celery 就自然而然了
```

### Brokers[消息队列]

```bash
brokers 中文意思为中间人，在这里就是指任务队列本身，Celery 扮演生产者和消费者的角色，
brokers 就是生产者和消费者存放/拿取产品的地方(队列)
常见的 brokers 有 rabbitmq、redis、Zookeeper 等
```

### Result Stores / backendp[数据存储]

```bash
顾名思义就是结果储存的地方，队列中的任务运行完后的结果或者状态需要被任务发送者知道，那么就需要一个地方储存这些结果，就是 Result Stores 了
常见的 backend 有 redis、Memcached 甚至常用的数据都可以
```

### Workers[消费者]

```bash
Celery 中的工作者，类似与生产/消费模型中的消费者，其从队列中取出任务并执行
```

### Tasks[队列中进行的任务]

```bash
队列中进行的任务，一般由用户、触发器或其他操作将任务入队，然后交由 workers 进行处理
```

## 准备工作

* 在Linux上单击部署Redis
* 安装python的redis依赖
* 安装python的celery依赖

## 在Linux上单击部署Redis

### 解压redis压缩文件

```bash
[root@sparsematrix ~]# mkdir -p /usr/local/redis/
[root@sparsematrix ~]# tar -zxvf redis-3.2.5.tar.gz -C /usr/local/redis/
```

### 进入redis目录

```bash
cd /usr/local/redis/
```

### 生成

```bash
[root@sparsematrix redis]# make
```
![All text](http://i1.piimg.com/581590/54cc599cecc213b9.png)

### 测试

```bash
[root@sparsematrix redis]# make test
#这段运行时间会较长
```

### 将redis的命令安装到/usr/bin/目录

```bash
[root@sparsematrix redis]# make install
```

![All text](http://i1.piimg.com/581590/f3bbec96d2ee8dd9.png)

### 运行Redis

#### 启动Redis服务器

```bash
[root@sparsematrix ~]# redis-server
```

![All text](http://i1.piimg.com/581590/3677acfcf6b8df60.png)

#### 启动客户端

```bash
redis-cli
```

![All text](http://i1.piimg.com/581590/51f59d8e34b82e97.png)

#### 执行命令

```bash
ping
set 'a' '123'
```

![All text](http://i1.piimg.com/581590/f4d07363ef92abf4.png)

```bash
当添加键值后，发现在当前运行的目录下，创建了一个文件：dump.rdb，这个文件用于将数据持久化存储
```

## 安装Python依赖

```bash
pip install redis
pip install celery
```

```bash
注意：如果你的 celery 是 4.0 及以上版本请确保 python 的 redis 库版本在 2.10.4 及以上，否则会出现 redis 连接 timeout 的错误
```

## Celery简单使用

### 编写任务代码

>server.py

```bash
# -*- coding:utf-8 -*-

import time
from celery import Celery

# Celery 的第一个参数是当前模块的名称，这个参数是必须的
app = Celery('server', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')  # 配置好celery的backend和broker


@app.task
def sendmail(mail):
    print('sending mail to %s ...' % mail['to'])
    time.sleep(2)
    print('mail send.')
    return 'Send Successful!'


# 装饰器app.task实际上是将一个正常的函数修饰成了一个 celery task 对象
@app.task()  # 普通函数装饰为 celery task
def add(x, y):
    return x + y
```

### 运行worker

```bash
在 tasks.py 所在目录下，运行worker
celery -A server worker --loglevel=info
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjzf1o7pijj215g0kd75n.jpg)

### 触发任务

>client.py

```bash
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

answer = sendmail.delay(dict(to='wanghaodi@lmbang.com'))
while not answer.ready():
    time.sleep(1)
print('task done: {0}'.format(result.get()))
```

```bash
delay 返回的是一个 AsyncResult 对象，里面存的就是一个异步的结果，当任务完成时result.ready() 为 true，然后用 result.get() 取结果即可
```

#### 运行结果

```bash
task done: 8
78a28c0a-3deb-4f6d-8b43-2c2e989d3ddc
task done: 8
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjzg2zqyshj21530l2jtl.jpg)

## 主函数分离

>app.py

```bash
# -*- coding: utf-8 -*-

# 主函数分离

from celery import Celery

app = Celery('app', include=['server'])
app.config_from_object('config')
```

>config.py

```bash
# -*- coding: utf-8 -*-

# 在任务调度中使用 msgpack 序列化，在任务结果中使用 json 序列化

BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']
```

>server.py

```bash
# -*- coding:utf-8 -*-

import time
from app import app


@app.task
def sendmail(mail):
    print('sending mail to %s ...' % mail['to'])
    time.sleep(2)
    print('mail send.')
    return 'Send Successful!'


# 装饰器app.task实际上是将一个正常的函数修饰成了一个 celery task 对象
@app.task()  # 普通函数装饰为 celery task
def add(x, y):
    return x + y
```

>client.py

```bash
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

answer = sendmail.delay(dict(to='xxxx@xxxx.com'))
# while not answer.ready():
#     time.sleep(1)
# print('task done: {0}'.format(answer.get()))

while 1:
    print('wait for ready')
    if answer.ready():
        break
    time.sleep(0.5)
print(answer.get())
```

### 启动celery服务器

```bash
celery -A app worker --loglevel=info
```

## 使用任务调度

```bash
任务调度的一种常见需求是每隔一段时间执行一遍任务，我们在配置文件中补充一些调度配置(config.py)
```

>config.py

```bash
# -*- coding: utf-8 -*-

from datetime import timedelta

# 在任务调度中使用 msgpack 序列化，在任务结果中使用 json 序列化

BROKER_URL = 'redis://127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
# CELERY_TASK_SERIALIZER = 'msgpack'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json', 'msgpack']

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULE = {
    'send-every-30-seconds': {
        'task': 'server.sendmail',
        # 'schedule': crontab(hour=16, minute=30),
        'schedule': timedelta(seconds=30),
        'args': (dict(to='sparsematrix@163.com'),)
    }
}
```

```bash
注意，任务的参数需为 元组 (tuple) 格式

启动 Celery ，因使用了调度配置，所以需加上 -B 参数
```

```bash
celery -A app worker -B -l info
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fk07r2sqx9j218t0loq5n.jpg)

## 在任务制定的文件中，我们增加一个指定时间执行的任务。(tasks.py)

>client.py

```bash
# -*- coding: utf-8 -*-

import time
from celery.schedules import crontab
from celery.task import periodic_task


@periodic_task(run_every=crontab(hour='16', minute='58'))
def schedule_sendmail():
    print('sending mail task')
    time.sleep(2)
    print('mail send.')
    return 'Send Successful！'
```

```bash
celery -A app worker -B -l info
```

## 使用多条队列

```bash
任务虽然是异步执行的，但是在任务执行的过程中，因为只有一条队列，所以任务执行是同步的

在 Celery 中，默认只有一条 celery 的队列，用于消息队列

在队列里任务一个一个的完成，这样的效率很低，我们可以创建多个队列，让多条队列同步进行

默认队列是 default
```

>config.py

```bash
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
CELERYBEAT_SCHEDULE = {
    'send-every-30-seconds': {
        'task': 'server.sendmail',
        # 'schedule': crontab(hour=16, minute=30),
        'schedule': timedelta(seconds=30),
        'args': (dict(to='sparsematrix@163.com'),)
    }
}

CELERY_QUEUES = (
    Queue('default', routing_key='task.#'),
    Queue('web_tasks', routing_key='web.#'),
)
```

>app.py

```bash
# -*- coding: utf-8 -*-

# 主函数分离

from celery import Celery

app = Celery('app', include=['server'])
app.config_from_object('config')
```

>server.py

```bash
# -*- coding:utf-8 -*-

import time
from app import app
from celery.utils.log import get_task_logger

# 记录日志和重试
logger = get_task_logger(__name__)


@app.task
def sendmail(mail):
    print('sending mail to %s ...' % mail['to'])
    time.sleep(2)
    print('mail send.')
    return 'Send Successful!'


# 装饰器app.task实际上是将一个正常的函数修饰成了一个 celery task 对象
@app.task()  # 普通函数装饰为 celery task
def add(x, y, queue='default'):
    logger.info('Executing server args: {}'
                'args: {}'.format(x, y))
    return x + y
```

>client.py

```bash
# -*- coding: utf-8 -*-

import time
from server import add
from celery.schedules import crontab
from celery.task import periodic_task


@periodic_task(run_every=crontab(hour='16', minute='58'))
def schedule_sendmail():
    print('sending mail task')
    time.sleep(2)
    print('mail send.')
    return 'Send Successful！'


if __name__ == "__main__":
    result = add.apply_async((1, 2), routing_key='task.add')
    result = add.apply_async(args=(1, 2), queue='default')
```

>仅开启单个路由

```bash
celery -A server worker -Q default -l info
```

>运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fk09i9j8clj213p0h30u2.jpg)

## 工作流

```bash
调用任务函数 add.delay(1,2) 的效果与 add.apply_async(args=(1,2)) 相同

使用 link 将第一个任务的结果作为第二个任务的参数
add.apply_async(args=(1,2), link=add.s(4))
```

### 过期时间

```bash
expires 单位为 秒，超过过期时间还未开始执行的任务会被回收
add.apply_async((1,2), expires=10)
```

### 并行调度

```bash
group , 一次调度多个任务，将任务结果以列表形式返回。

In [16]: from celery import group
In [17]: res = group(add.s(i, i) for i in xrange(10))()
In [18]: res.get()
Out[18]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

### 串行调度

```bash
chain , 一次调度多个任务，将前一个任务的结果作为参数传入下一个任务

In [19]: from celery import chain
In [20]: res = chain(add.s(2, 2), add.s(4), add.s(8))()
In [21]: res.get(timeout=1)
Out[21]: 16
```
