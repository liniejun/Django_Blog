from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown

# Create your views here.
def index(request):
    #  文章按照创建时间倒序排列，即最新的排在最前面
    post_list = Post.objects.order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.content = markdown.markdown(post.content, extensions=['markdown.extensions.extra',
                                                               'markdown.extensions.codehilite',
                                                               'markdown.extensions.toc',])
    return render(request, 'blog/detail.html', context={'post': post})

