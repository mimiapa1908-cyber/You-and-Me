from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/like/<int:post_id>/', views.like_post, name='like_post'),
]
