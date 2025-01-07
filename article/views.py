from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Article, Category, ArticleTags
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


class ArticleView(View):
    template_name = 'article/article.html'

    def get(self, request, category_slug=None, tag_slug=None):
        articles = Article.objects.filter(status=True)
        paginator = Paginator(articles, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        categories = Category.objects.all()
        tags = ArticleTags.objects.all()
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            articles = articles.filter(category=category)
        if tag_slug:
            tag = ArticleTags.objects.get(slug=tag_slug)
            articles = articles.filter(tag=tag)
        return render(request, self.template_name, {'articles': page_obj, 'categories': categories, 'tags': tags})


class ArticleDetailView(View):
    def get(self, request, article_slug=None):
        article = get_object_or_404(Article, slug=article_slug)
        return render(request, 'article/detail.html', {'article': article})

class ArticleDeleteView(LoginRequiredMixin, View):
    def get(self, request, article_id):
        article = Article.objects.get(pk=article_id)
        if article.author.id == request.user.id:
            article.delete()
            messages.success(request, 'Article deleted successfully', 'success')
            return redirect('account:user profile', request.user.id)
        else:
            messages.error(request, 'You can not delete this article', 'danger')
        return redirect('home:home')
