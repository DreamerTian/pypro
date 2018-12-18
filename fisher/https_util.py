# _*_ encoding:utf-8 _*_
__author__ = ''
__date__ = '2018/12/14 10:42'

import requests


class HTTP:
    def get(self, url, return_json=True):
        r = requests.get(url)

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text


