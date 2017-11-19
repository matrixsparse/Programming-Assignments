#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import logging

# from cloghandler import ConcurrentRotatingFileHandler
#
#
# def get_logger(logfile='lalabot.log'):
#     """
#     日志模块
#     :param logfile: 文件名
#     :return:
#     """
#     logger = logging.getLogger(logfile)
#     logger.setLevel(logging.DEBUG)
#     rotateHandler = ConcurrentRotatingFileHandler(logfile, 'a', 100 * 1024 * 1024, backupCount=10, encoding='utf-8')
#     datefmt_str = '%Y-%m-%d %H:%M:%S'
#     format_str = '%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s'
#     formatter = logging.Formatter(format_str, datefmt_str)
#     rotateHandler.setFormatter(formatter)
#     logger.addHandler(rotateHandler)
#     return logger
