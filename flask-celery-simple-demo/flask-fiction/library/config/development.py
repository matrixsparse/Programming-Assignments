#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix


import os


class Config:
    DEBUG = False

    # 授权token
    AUTH_TOKEN = {'64233ea4dbt69ssa535011afe0269a2b', '866526ac824s8a67t9c5be23c40748ya'}

    # 发送邮件
    MAIL_CONFIG = {
        'server': 'smtp.exmail.qq.com',
        'port': 25,
        'send_from': 'wanghaodi@lmbang.com',
        'user': 'wanghaodi@lmbang.com',
        'password': 'sadasdasdada',
        'send_to': 'sparsematrix@163.com'
    }

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    # redis配置
    REDIS_CONFIG = {
        'default': {
            'host': 'localhost',
            'port': 6379,
            'db': 0
        }
    }

    # DB配置
    DB_CONFIG = {
        'db_chatplus': {
            'dialect': 'mysql',
            'driver': 'mysqldb',
            'host': '',
            'port': 3306,
            'user': '',
            'password': '',
            'database': '',
            'charset': 'utf8mb4'
        },
        'db_chatplus_proxy': {
            'dialect': 'mysql',
            'driver': 'mysqldb',
            'host': '',
            'port': '',
            'user': '',
            'password': '',
            'database': '',
            'charset': 'utf8'
        }
    }


class BetaConfig(Config):
    # beta
    DEBUG = True

    # redis配置
    REDIS_CONFIG = {
        'default': {
            'host': 'localhost',
            'port': 6379,
            'db': 0
        }
    }

    # DB配置
    DB_CONFIG = {
        'db_chatplus': {
            'dialect': 'mysql',
            'driver': 'mysqldb',
            'host': '',
            'port': 3306,
            'user': '',
            'password': '',
            'database': '',
            'charset': 'utf8mb4'
        },
        'db_chatplus_proxy': {
            'dialect': 'mysql',
            'driver': 'mysqldb',
            'host': '',
            'port': '',
            'user': '',
            'password': '',
            'database': '',
            'charset': 'utf8'
        }
    }


class ProductionConfig(Config):
    # production
    DEBUG = True

    # redis配置
    REDIS_CONFIG = {
        'default': {
            'host': 'localhost',
            'port': 6379,
            'db': 0
        }
    }

    # DB配置
    DB_CONFIG = {
        'db_chatplus': {
            'dialect': 'mysql',
            'driver': 'mysqldb',
            'host': '',
            'port': 3306,
            'user': '',
            'password': '',
            'database': '',
            'charset': 'utf8mb4'
        },
        'db_chatplus_proxy': {
            'dialect': 'mysql',
            'driver': 'mysqldb',
            'host': '',
            'port': '',
            'user': '',
            'password': '',
            'database': '',
            'charset': 'utf8'
        }
    }


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    'beta': BetaConfig
}.get(os.getenv('FLASK_CONFIG') or 'default', BetaConfig)
