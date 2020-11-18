#! /usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : declan
# @Time    : 2020/11/17 21:31
# @File    : __init__.py.py
# @Software: PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import config_dict

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    config = config_dict(config_name)
    app.config.from_object(config)

    db.init_app(app)
    return app
