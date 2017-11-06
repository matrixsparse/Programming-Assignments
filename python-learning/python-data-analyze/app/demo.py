#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

from flask import Flask, request, render_template
from flask.ext.uwsgi_websocket import GeventWebSocket

app = Flask(__name__)
ws = GeventWebSocket(app)


@app.route('/')
def index():
    return render_template('index.html')


@ws.route('/foobar')
def echo(wscon):
    msg = wscon.receive()
    if msg is not None:
        ws.send(msg)


if __name__ == '__main__':
    app.run(gevent=100)
