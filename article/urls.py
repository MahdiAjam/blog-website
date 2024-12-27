from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.ArticleView.as_view(), name='article'),
    path('category/<slug:category_slug>/', views.ArticleView.as_view(), name='article category'),
    path('detail/<slug:article_slug>/', views.ArticleDetailView.as_view(), name='article detail'),
]