from django.contrib import admin

# Register your models here.
from .models import Post, Group

""" Чтобы в админке были видны наши модели регистрируем их тут """

class PostAdmin(admin.ModelAdmin):
    """ Перечисляем поля для отображения в таблице """
    list_display = ("pk", "text", "pub_date", "author")
    """ Перечисляем поля по которым можно будет искать  """
    search_fields = ("text",)
    """ фильтр """
    list_filter = ("pub_date",)
    """ если пусое значение то... """
    empty_value_display = "-пусто-"

class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description")
    search_fields = ("title", "description")
    empty_value = "-пусто-"
    
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
