from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

""" Модели должны быть зарегистрированы в admin.py """


class Post(models.Model):
    """ описание поста """
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="posts")
    # создаем связь поста с сообществом
    group = models.ForeignKey("Group", on_delete=models.SET_NULL,
                              blank=True,
                              null=True,
                              related_name="posts")

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.text


class Group(models.Model):
    """ описание сообщества """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=100, default="")

    def __str__(self):
        """ Выводим поле title"""
        return self.title
