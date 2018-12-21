# _*_ encoding:utf-8 _*_
from flask import Blueprint

__author__ = ''
__date__ = '2018/12/21 13:35'

web = Blueprint('web', __name__)

from app.web import book