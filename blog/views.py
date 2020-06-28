from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CommentForm
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


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    extra_context = {'blog': Blog.objects.all, 'title': 'New comment', }
