from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user register'),
    path('verify/', views.RegisterVerifyCode.as_view(), name='verify_code'),
    path('login/', views.UserLoginView.as_view(), name='user login'),
    path('logout/', views.UserLogoutView.as_view(), name='user logout'),
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='user profile'),
    path('edit/<int:pk>/', views.UserEditProfileView.as_view(), name='user edit profile'),
    path('reset/', views.UserPasswordResetView.as_view(), name='reset password'),
    path('reset/done/', views.UserPasswordDoneView.as_view(), name='password reset done'),
    path('confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='password reset confirm'),
    path('confirm/complete/', views.UserPasswordResetCompleteView.as_view(), name='password reset complete'),
]
