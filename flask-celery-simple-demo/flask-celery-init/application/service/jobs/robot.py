# -*- coding: utf-8 -*-

from application.service.cele import app

@app.task
def send(message):
    return message