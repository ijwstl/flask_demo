# -*- coding: utf-8 -*-

"""
@author: ijwstl
@software: PyCharm
@file: utils_api.py
@time: 8/6/2023 10:00 PM
"""
from flask import Blueprint
from app.src.entity.UserEntity import User

bp = Blueprint(name="utils", import_name=__name__, url_prefix="/utils")


@bp.route("/demo")
def demo():
    """
    @description:

    ------------
    @params:

    ------------
    @return:

    """
    a = User.query.first()
    print(a)
    return "123"