#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Shawn Lee'

from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url(r'^comment/post/(?P<post_id>[0-9]+)/$', views.post_comment, name='post_comment')
]