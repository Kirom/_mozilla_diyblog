from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from blog.models import Blog, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'post_datetime', 'edit_datetime', 'link_to_user', ]

    # Генерация ссылки на пользователя с конкретного поста
    def link_to_user(self, obj):
        link = reverse("admin:auth_user_change", args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', link, obj.author.username)

    link_to_user.short_description = 'Пользователь'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'post_datetime', 'edit_datetime', 'author', 'link_to_blog']

    def link_to_blog(self, obj):
        link = reverse("admin:blog_blog_change", args=[obj.blog.pk])
        return format_html('<a href="{}">{}</a>', link, obj.blog.title)

    link_to_blog.short_description = 'Блог'
