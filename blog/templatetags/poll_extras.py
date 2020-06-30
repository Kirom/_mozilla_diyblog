from django import template

register = template.Library()


@register.filter(name='blog_title_detail')
def blog_title_detail(value, arg):
    # Создание своего(кастомного) фильтра
    # value = Blog QuerySet
    # arg = id блога
    # Возвращает название блога с id (arg)
    return value.get(id=arg)
    # return value.filter(book__exact=arg, status__exact='a').count()


# @register.filter(name='blog_post_datetime')
# def blog_post_datetime(value, arg):
#     return value.get(id=arg).post_datetime
