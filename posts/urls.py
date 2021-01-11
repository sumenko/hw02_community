from django.urls import path

# Из текущей папки подключаем views.py
from . import views
# not urlSpatterns
urlpatterns = [
    path("", views.index, name="index"),
    path("groups/", views.group_posts),
    path("groups/<slug:slug>/", views.group_posts),
]