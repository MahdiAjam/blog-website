from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user register'),
    path('verify/', views.RegisterVerifyCode.as_view(), name='verify_code'),
    path('login/', views.UserLoginView.as_view(), name='user login'),
    path('logout/', views.UserLogoutView.as_view(), name='user logout'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='user profile'),
]