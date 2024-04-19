from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('create/',views.create_post,name='create'),
    path('<int:pk>/',views.post_detail, name='post_detail'),
    path('<int:pk>/update', views.post_update, name='post_update'),
    path('<int:pk>/delete', views.post_delete, name='post_delete'),
    path('<int:pk>/like', views.post_like, name='post_like'),
    path('search/', views.search_results, name='search_results'),
]
