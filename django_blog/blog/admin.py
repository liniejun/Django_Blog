# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_time', 'modified_time', 'category', 'author']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 10



admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)