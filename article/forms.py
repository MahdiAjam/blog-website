from django import forms
from .models import Article

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'category', 'tag', 'image', 'description', 'status')
