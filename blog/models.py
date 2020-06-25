from django.contrib.auth.models import User
from django.db import models

# class Author(models.Model):
#     first_name = models.CharField(max_length=100, verbose_name='Имя')
#     last_name = models.CharField(max_length=100, verbose_name='Фамилия')
#     nickname = models.CharField(max_length=100, verbose_name='Никнейм')

# if self.is_authorized -> return self.username
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название', help_text='Название поста блога')
    content = models.TextField(verbose_name='Содержание', help_text='Содержание поста')
    post_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    edit_datetime = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)
    author = models.ForeignKey('auth.user', verbose_name='Автор', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.pk)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name='Содержание', help_text='Содержание комментария')
    post_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    edit_datetime = models.DateTimeField(auto_now=True, verbose_name='Дата изменения', null=True)
    author = models.ForeignKey('auth.user', verbose_name='Автор', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name='Пост блога', on_delete=models.CASCADE)
