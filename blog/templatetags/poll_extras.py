from django import template

register = template.Library()


def blog_title_detail(value, arg):
    # Создание своего(кастомного) фильтра
    # value = Blog QuerySet
    # arg = id блога
    # Возвращает название блога с id (arg)
    return value.get(id=arg)
    # return value.filter(book__exact=arg, status__exact='a').count()


register.filter('blog_title_detail', blog_title_detail)
