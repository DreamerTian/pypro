# _*_ encoding:utf-8 _*_
from flask import jsonify
import requests

__author__ = ''
__date__ = '2018/12/14 10:42'


class HTTP:

    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return jsonify({'msg': '返回信息错误'}) if return_json else ''
        return jsonify(r.json())if return_json else r.text


