#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

from service.application import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)  # 运行flask http程序，host指定监听IP，port指定监听端口，调试时需要开启debug模式
