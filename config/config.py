#! /usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : declan
# @Time    : 2020/11/17 21:34
# @File    : config.py
# @Software: PyCharm
class Config:
    DEBUG = True
    JSON_AS_ASVCII=False
    #
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:root@127.0.0.1:3306'
    SQLALCHEMY_TRACK_MODIFICATIONS=


class DevConfig(Config):
    pass


class ProConfig(Config):
    pass


class TestConfig(Config):
    pass


config_dict = {
    'dev': DevConfig,
    'pro': ProConfig,
    'test': TestConfig,
}
