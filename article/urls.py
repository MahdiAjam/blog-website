from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.ArticleView.as_view(), name='article'),

]