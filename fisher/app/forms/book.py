# _*_ encoding:utf-8 _*_
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange

__author__ = ''
__date__ = '2018/12/21 14:27'


class SearchForm(Form):

    q = StringField(validators=[Length(min=1, max=31)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)

