from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']

class EditArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'thumb']