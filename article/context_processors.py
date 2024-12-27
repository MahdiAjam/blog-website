from article.models import Article, Category, ArticleTags

def articles_and_categories(request):
    articles = Article.objects.filter(status=True)
    categories = Category.objects.all()
    return {'articles': articles, 'categories': categories}

def tags(request):
    tag = ArticleTags.objects.all()
    return {'tags': tag}
