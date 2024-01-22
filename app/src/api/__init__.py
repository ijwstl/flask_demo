# -*- coding: utf-8 -*-

"""
@author: ijwstl
@software: PyCharm
@file: __init__.py.py
@time: 8/6/2023 10:00 PM
"""
from typing import List
from flask import Flask, Blueprint
from app.src.api.utils_api import bp as utils_bp


api_list: List[Blueprint] = [utils_bp]


def register_api(app: Flask):
    for bp in api_list:
        app.register_blueprint(bp)


__all__ = [
    "register_api"
]
