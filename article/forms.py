from django import forms
from .models import Article


class ArticleUpdateCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('category', 'title', 'tag', 'image', 'description', 'status')
