# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.
# python_2_unicode_compatible 用于兼容python2
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    abstract = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    read_count = models.IntegerField(default=0)
    content_count = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # 'blog:detail'，意思是 blog 应用下的 name=detail 的函数
        # 由于我们在上面通过 app_name = 'blog' 告诉了 Django 这个 URL 模块是属于 blog 应用的，
        # 因此 Django 能够顺利地找到 blog 应用下 name 为 detail 的视图函数，
        # 于是 reverse 函数会去解析这个视图函数对应的 URL
        return reverse('blog:detail', kwargs={'id':self.id})

    def Meta(self):
        ordering = ['-create_time']
