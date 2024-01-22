# -*- coding: utf-8 -*-

"""
@author: ijwstl
@software: PyCharm
@file: __init__.py.py
@time: 8/6/2023 9:32 PM
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.src.config.app_config import config


db = SQLAlchemy()


def init_database(app: Flask):
    db.init_app(app)


__all__ = [
    "db",
    "init_database",
    "config"
]
