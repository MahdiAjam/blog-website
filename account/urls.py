from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify/', views.RegisterVerifyCode.as_view(), name='verify_code'),
    path('login/', views.LoginView.as_view(), name='login'),

]