#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Shawn Lee'

from django import template
from ..models import Post, Category

register = template.Library()

# 获取数据库的最近5篇文章
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')

@register.simple_tag
def get_categorys():
    return Category.objects.all()