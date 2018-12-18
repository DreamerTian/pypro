# _*_ encoding:utf-8 _*_
__author__ = ''
__date__ = '2018/12/12 14:49'

from flask import Flask
from fisher.helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q
        page
    :return:
    """
    # isbn
    isbn_or_key = is_isbn_or_key(q)


    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8181', debug=app.config['DEBUG'])

