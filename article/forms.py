from django import forms
from .models import Article, Comment


class ArticleUpdateCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('category', 'title', 'tag', 'image', 'description', 'status')

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
