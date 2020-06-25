from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Blog, Comment


def home(request):
    return render(request, 'Homepage.html', )


class BlogListView(ListView):
    model = Blog
    paginate_by = 5

    def get_ordering(self):
        return '-post_datetime'


class BlogDetailView(DetailView):
    model = Blog
    extra_context = {'comments': Comment.objects.all}
