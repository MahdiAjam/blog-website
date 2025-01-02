from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article, Category, ArticleTags


class ArticleView(View):
    template_name = 'article/article.html'

    def get(self, request, category_slug=None, tag_slug=None):
        articles = Article.objects.filter(status=True)
        categories = Category.objects.all()
        tags = ArticleTags.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            articles = articles.filter(category=category)
        if tag_slug:
            tag = ArticleTags.objects.get(slug=tag_slug)
            articles = articles.filter(tag=tag)
        return render(request, self.template_name, {'articles': articles, 'categories': categories, 'tags': tags})


class ArticleDetailView(View):
    def get(self, request, article_slug=None):
        article = get_object_or_404(Article, slug=article_slug)
        return render(request, 'article/detail.html', {'article': article})

