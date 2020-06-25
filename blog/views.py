from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Blog


def home(request):
    return render(request, 'Homepage.html', )


class BlogListView(ListView):
    model = Blog
    paginate_by = 5

    def get_ordering(self):
        return '-post_datetime'
