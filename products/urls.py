from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('create/',views.create_post,name='create'),
    path('<int:pk>/',views.post_detail, name='post_detail'),
]
