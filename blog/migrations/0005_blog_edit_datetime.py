# Generated by Django 3.0.7 on 2020-06-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200621_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='edit_datetime',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения'),
        ),
    ]
