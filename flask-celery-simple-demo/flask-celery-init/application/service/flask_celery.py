# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

from celery import Celery
from celery import platforms  # 如果你不是linux的root用户，这两行没必要
from celery.schedules import crontab

platforms.C_FORCE_ROOT = True  # 允许root权限运行celery


def make_celery(app):
    celery = Celery('flask_celery',  # 此处官网使用app.import_name，因为这里将所有代码写在同一个文件flask_celery.py,所以直接写名字。
                    broker=app.config['CELERY_BROKER_URL'],
                    backend=app.config['CELERY_RESULT_BACKEND']
                    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/1'
)
celery = make_celery(app)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=17, minute=36),
        test.s('Happy Mondays!'),
    )


@celery.task
def test(arg):
    print(arg)


@celery.task()
def long_time_def():
    for _ in range(10000):
        for j in range(10000):
            i = 1
    return 'hello'


@app.route("/")
def hello():
    print("耗时的任务")
    result = long_time_def.apply_async()  # 变化在这里
    return '耗时的任务已经交给了celery'


if __name__ == '__main__':
    app.run(host='115.28.240.96', port=12503, debug=True)
