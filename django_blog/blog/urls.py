#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Shawn Lee'

from django.conf.urls import url
from . import views

# 视图函数命名空间
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<id>[0-9]+)/$', views.detail, name='detail'),
]