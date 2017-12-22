from django.shortcuts import render, get_object_or_404
from .models import Post, Category
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

def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=category).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


