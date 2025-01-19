from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.ArticleView.as_view(), name='article'),
    path('category/<slug:category_slug>/', views.ArticleView.as_view(), name='article category'),
    path('tags/<slug:tag_slug>', views.ArticleView.as_view(), name='article tag'),
    path('detail/<slug:article_slug>/', views.ArticleDetailView.as_view(), name='article detail'),
    path('delete/<int:article_id>/', views.ArticleDeleteView.as_view(), name='article delete'),
    path('update/<int:article_id>/', views.ArticleUpdateView.as_view(), name='article update'),
    path('create/', views.ArticleCreateView.as_view(), name='article create'),
    path('reply/<int:article_id>/<int:comment_id>/', views.CommentReplyView.as_view(), name='comment reply'),
]