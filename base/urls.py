
from django.urls import path
from knox import views as knox_views

from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('api/', views.Routes, name="Routes"),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('api/bikes', views.bikesList.as_view(), name="bikesList"),
    path('api/bikes/<str:pk>/', views.bikesDetail.as_view(), name="bikesDetail"),
    path('api/category/', views.categoryList.as_view(), name="categoryList"),
    path('api/category/<str:pk>/',
         views.categoryDetail.as_view(), name="categoryDetail"),

    path('api/carts', views.ListCart.as_view(), name="allcarts"),
    path('api/carts/<str:pk>', views.DetailCart.as_view(), name="cartdetail"),


]
