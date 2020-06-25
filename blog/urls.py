from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^all/$', views.BlogListView.as_view(), name='all'),
]
