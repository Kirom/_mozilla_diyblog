from django import forms
from django.contrib.auth.models import User

from .models import Comment, Blog


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Комментарий',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'placeholder': 'Текст комментария', 'cols': 10,
                                         'rows': 10}))

    # author = forms.ModelChoiceField(User.objects, widget=forms.HiddenInput())
    # blog = forms.ModelChoiceField(Blog.objects, widget=forms.HiddenInput())

    class Meta(object):
        model = Comment
        fields = ['content', ]
