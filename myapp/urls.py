from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('gallery/', views.gallery, name='gallery'),
    path('videos/', views.videos, name='videos'),




]
