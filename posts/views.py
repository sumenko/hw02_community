from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
# Create your views here.

def index(request):
    latest = Post.objects.all() #.order_by('-pub_date')[:10]
    # собираем тексты постов в один, разделяя новой строкой
    # output = [item.text for item in latest]
    # return HttpResponse("<br><br>\n".join(output))

    return render(request, "index.html", {"posts": latest})

def group_posts(request, slug=None, path=None):

    
    pass
