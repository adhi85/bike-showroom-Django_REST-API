
from django.urls import path
from . import views
urlpatterns = [
    # path('',views.home, name="home")
     path('api/register/', views.RegisterAPI.as_view(), name='register'),
]
