# Generated by Django 3.0.7 on 2020-06-21 12:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(help_text='Содержание поста', verbose_name='Содержание'),
        ),
    ]
