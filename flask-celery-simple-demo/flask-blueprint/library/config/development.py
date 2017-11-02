#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix


import os


class Config:
    DEBUG = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    # redis配置
    REDIS_CONFIG = {
        'default': {
            'host': '',
            'port': 7403,
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


class TestingConfig(Config):
    # 249环境
    DEBUG = True

    # redis配置
    REDIS_CONFIG = {
        'default': {
            'host': '',
            'port': 7403,
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
    DEBUG = True

    # redis配置
    REDIS_CONFIG = {
        'default': {
            'host': '',
            'port': 7403,
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
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    'beta': TestingConfig
}.get(os.getenv('FLASK_CONFIG') or 'default', DevelopmentConfig)
