from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control custom-txt', 'cols': '40', 'rows': '3'}), label='')

    class Meta:
        model = Comment
        fields = ['body',]
