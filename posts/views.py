from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse

from .models import Post, Group


def index(request):
    """ Вывод последних 10 постов из базы """
    latest = Post.objects.order_by('-pub_date')[:10]
    return render(request, "index.html", {"posts": latest})


def group_posts(request, slug=None):
    # Получаем объект из базы соответствующий slug
    group = get_object_or_404(Group, slug=slug)
    # Получаем все посты принадлежащие slug
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})
