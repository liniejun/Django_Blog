from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    #  文章按照创建时间倒序排列，即最新的排在最前面
    post_list = Post.objects.order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

