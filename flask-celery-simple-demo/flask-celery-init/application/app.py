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
