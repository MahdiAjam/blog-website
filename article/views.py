from django.shortcuts import render
from django.views import View
class ArticleView(View):
    def get(self, request):
        return render(request, 'article/article.html')
