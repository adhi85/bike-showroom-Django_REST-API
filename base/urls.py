
from django.urls import path
from knox import views as knox_views

from . import views
urlpatterns = [
    path('',views.home, name="home"),
    path('api/',views.Routes, name="Routes"),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
