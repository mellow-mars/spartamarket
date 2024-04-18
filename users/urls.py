from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/follow', views.follow, name='follower'),
]
