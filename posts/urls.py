from django.urls import path

# Из текущей папки подключаем views.py
from . import views
# not urlSpatterns
""" у нас два варианта: вывод всех постов или по сообществу """
urlpatterns = [
    path("", views.index, name="index"),
    path("group/<slug:slug>/", views.group_posts),
]
