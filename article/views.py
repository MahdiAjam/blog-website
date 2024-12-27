from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article, Category


class ArticleView(View):
    template_name = 'article/article.html'

    def get(self, request, category_slug=None):
        articles = Article.objects.filter(status=True)
        categories = Category.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            articles = articles.filter(category=category)
        return render(request, self.template_name, {'articles': articles, 'categories': categories})


class ArticleDetailView(View):
    def get(self, request, article_slug=None):
        article = get_object_or_404(Article, slug=article_slug)
        return render(request, 'article/detail.html', {'article': article})
