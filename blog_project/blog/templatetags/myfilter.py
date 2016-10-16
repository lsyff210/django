# coding:utf-8
from django import template

register = template.Library()


@register.filter
def month_cn_upper(value):
    month_orig = int(value.month)
    month_cn = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '十一', '十二']
    month_get = month_cn[month_orig-1]
    return month_get
