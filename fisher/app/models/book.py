# _*_ encoding:utf-8 _*_
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

__author__ = ''
__date__ = '2018/12/21 16:26'

db = SQLAlchemy()


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    isbn = Column(String(15), nullable=False, unique=True)

    def sample(self):
        pass

