# -*- coding: utf-8 -*-

"""
@author: ijwstl
@software: PyCharm
@file: __init__.py.py
@time: 8/6/2023 9:25 PM
"""
import logging.config
import logging
from flask import Flask
from app.src.api import register_api
from app.src.config import init_database, config


def create_app() -> Flask:
    """
    @description:

    ------------
    @params:

    ------------
    @return:

    """

    app = Flask(__name__)
    app.config.from_object(config.get("development"))

    logging.config.fileConfig(r"D:\\Code_Project\\Python_Project\\flask\\app\\logging.conf")
    lg = logging.getLogger("myLogger")
    a = {
        "123": 123}
    init_database(app)
    lg.info("-------init_database-------")
    register_api(app)
    lg.info("-------register_api-------")
    return app
