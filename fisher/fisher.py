# _*_ encoding:utf-8 _*_
__author__ = ''
__date__ = '2018/12/12 14:49'

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    return 'Hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8181', debug=app.config['DEBUG'])

