#! /usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : declan
# @Time    : 2020/11/17 21:30
# @File    : manager.py
# @Software: PyCharm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import MigrateCommand

app = Flask(__name__)
db = SQLAlchemy(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run()
