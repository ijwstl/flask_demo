# -*- coding: utf-8 -*-

"""
@author: ijwstl
@software: PyCharm
@file: UserEntity.py
@time: 8/6/2023 9:49 PM
"""
from app.src.config import db


class User(db.Model):

    """

        USER: ijwstl
        DATE:
        FILENAME: ${NAME}.py
        ClASSNAME: User

    """

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, nullable=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
