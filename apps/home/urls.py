from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]