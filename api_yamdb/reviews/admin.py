from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, Comment, Genre, Review, Title, User


class GenreAdmin(admin.ModelAdmin):
    """Класс нужен для вывода на странице админа
    информации по жанрам."""

    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    """Класс нужен для вывода на странице админа
    информации по категориям."""

    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    """Класс нужен для вывода на странице админа
    информации по названиям произведений."""

    list_display = ('pk', 'name', 'year', 'description')
    search_fields = ('name', 'description')
    list_filter = ('year',)
    empty_value_display = '-пусто-'


class ReviewAdmin(admin.ModelAdmin):
    """Класс нужен для вывода на странице админа
    информации по отзывам."""

    list_display = ('id', 'author', 'pub_date', 'score', 'title', 'text')
    search_fields = ('author', 'title', 'text')
    list_filter = ('author', 'pub_date')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    """Класс нужен для вывода на странице админа
    информации по комментариям."""

    list_display = ('id', 'author', 'pub_date', 'review', 'text')
    search_fields = ('review', 'text')
    list_filter = ('author', 'pub_date')
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
