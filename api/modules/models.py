#! /usr/bin/python
# -*- coding: utf-8 -*-
# @Author  : declan
# @Time    : 2020/11/17 22:42
# @File    : models.py
# @Software: PyCharm
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from api import db


class BaseModels:
    """模型基类"""
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录你的更新时间


class UserInfo(BaseModels, db.Model):
    """用户信息表"""
    __tablename__ = "user_info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 用户id
    nickname = db.Column(db.String(64), nullable=False)  # 用户昵称
    mobile = db.Column(db.String(16))  # 手机号
    avatar_url = db.Column(db.String(256))  # 用户头像路径
    signature = db.Column(db.String(256))  # 签名
    sex = db.Column(db.Enum('0', '1', '2'), default='0')  # 1男 2 女 0 不确定
    birth_date = db.Column(db.DateTime)  # 出生日期
    role_id = db.Column(db.Integer)  # 角色id

    def add(self):
        pass

    def update(self):
        pass

    def to_dict(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'mobile': self.mobile,
            'avatar_url': self.avatar_url,
        }


class UserLogin(BaseModels):
    pass
