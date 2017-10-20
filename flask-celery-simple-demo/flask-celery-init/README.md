# flask和celery结合

## 配置 Celery

```bash
你需要的第一个东西是一个 Celery 实例，称为 Celery 应用。

仅就 Celery 而言 其与 Flask 中的 Flask 对象有异曲同工之妙

在 Celery 中做任何事——诸如创建任务和管理职程（Worker）——的入口点， 它必须可以在其它模块中导入

例如，你可以把它放置到 tasks 模块中

虽然你可以在不重新配置 Flask 的 情况下使用 Celery，
但继承任务、添加对 Flask 应用上下文的支持以及关联 Flask 配置会让情况变得更好
```

>app.py

```bash
# -*- coding: utf-8 -*-
import time
from celery import Celery
from flask import Flask

app = Flask(__name__)

app.config['CELERY_TASK_SERIALIZER'] = 'json'
app.config['CELERY_RESULT_SERIALIZER'] = 'json'

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task()
def add(a, b):
    return a + b


@app.route('/', methods=['GET'])
def longtask():
    result = add.delay(22, 23)
    while not result.ready():
        time.sleep(1)
    return ('task done: {0}'.format(result.get()))


if __name__ == '__main__':
    app.run(host='115.28.240.96', port=12503, debug=True)
```

### 启动Celery服务

```bash
celery worker -A app.celery -l INFO  -B
```

## 运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fk0j17b1cuj215i0ltq4k.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fk0is5qfsnj20qe052t8n.jpg)

## Celery定时任务

>cele.py

```bash
# -*- coding: utf-8 -*-

import celery
from celery.schedules import crontab

app = celery.Celery('cele', broker='redis://localhost:6379/0')


@app.task
def send(message):
    return message


app.conf.beat_schedule = {
    'send-every-60-seconds': {
        'task': 'cele.send',
        # 每两小时执行一次
        # 'schedule': 3600.0,

        # 每十五分钟执行一次
        'schedule': crontab(minute='*/1'),
        'args': ('Hello World',)
    },
}
```

>执行

```bash
celery -A cele worker -l info -B
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fkorn67s90j20tg0lx75p.jpg)
