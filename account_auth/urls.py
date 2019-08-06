from . import views


urlpatterns = [
    
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.HomePageView.as_view(), name='home')
]