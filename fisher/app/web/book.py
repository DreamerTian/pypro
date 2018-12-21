# _*_ encoding:utf-8 _*_
from flask import request, jsonify
from app.libs.helper import is_isbn_or_key
from app.forms.book import SearchForm

from app.spider.yushu_book import YuShuBook
from . import web

__author__ = ''
__date__ = '2018/12/21 11:47'


@web.route('/book/search')
def search():
    """
        q
        page
    :return:
    """

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        # isbn
        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)

        return result
    else:
        return jsonify({'msg': '参数校验失败'})

