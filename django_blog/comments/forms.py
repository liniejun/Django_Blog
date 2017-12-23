#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Shawn Lee'

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']

