from django import forms

from .models import Comment, Blog


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='Комментарий',
                              widget=forms.Textarea(
                                  attrs={'class': 'form-control', 'placeholder': 'Текст комментария', 'cols': 3,
                                         'rows': 10}))

    # blog = forms.ModelChoiceField(queryset=Blog.objects, )

    class Meta(object):
        model = Comment
        fields = ('content',)
