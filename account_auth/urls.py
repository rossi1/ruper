from django.contrib.auth import views as auth_views
from django.urls import path

from . import views




urlpatterns = [
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', views.HomePageView.as_view(), name='home')
]