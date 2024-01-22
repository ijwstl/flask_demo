# -*- coding: utf-8 -*-

"""
@author: ijwstl
@software: PyCharm
@file: app_config.py
@time: 8/6/2023 9:32 PM
"""


class BaseConfig:

    """
    
        USER: ijwstl
        DATE:
        FILENAME: ${NAME}.py
        ClASSNAME: FlaskConfig
        
    """
    # TODO 需要测试一下
    DEBUG = True

    SQLALCHEMY_BINDS = {
        "DEMO": {
            "url": "mysql+pymysql://root:123456@192.168.124.10:5306/flask?charset=utf8",
            "pool_size": 5, "pool_recycle": 3600
        }
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_ECHO = False


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
