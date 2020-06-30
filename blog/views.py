import datetime
import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
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

    def get_success_url(self):
        return reverse('blog:detail', kwargs={'pk': self.kwargs['pk']})
        # Прошлая моя реализация (facepalm)
        # return self.request.path[:-6]

    # def get_initial(self):
    #     """
    #     Моя реализация.
    #     Для работы необходимо в forms.py включить поля author, blog в саму форму и в fields класса Meta.
    #     """
    #     author = self.request.user
    #     blog_id = re.findall(r'/blog/(\d+)/.*', self.request.path)
    #     blog = get_object_or_404(Blog, id=int(blog_id[0]))
    #     return {'author': author, 'blog': blog}

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        print(self.kwargs)
        return super(CommentCreateView, self).form_valid(form)
