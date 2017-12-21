from django.contrib import admin

# Register your models here.
from django_blog.blog.models import Category, Tag, Post
from django.utils import timezone
from django.contrib.auth.models import User

# 创建分类和标签
c = Category(name='python')
c.save()
t = Tag(name='数据库')
t.save()

# 新建一篇文章
user = User.objects.get(username='admin')
c = Category.objects.get(name='python')
p =Post(title='我爱django', content='保持学习的热情很重要啊', create_time=timezone.now(), modified_time=timezone.now(), category=c, author=user)
p.save()

Post.objects.all()