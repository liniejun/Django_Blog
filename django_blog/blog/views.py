from django.shortcuts import render
from datetime import datetime
# Create your views here.
def helloworld(request):
    context = {'current_time': datetime.now()}
    return render(request, 'blog/helloworld.html', context)