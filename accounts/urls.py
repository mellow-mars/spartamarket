from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    진우 바보
    path('<str:username>/update', views.update, name='update'),
    path('<str:username>/delete', views.delete, name='delete'),
    path('<str:username>/password', views.change_password, name='change_password'),
]

