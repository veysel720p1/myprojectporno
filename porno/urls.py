from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.category_videos, name='category_videos'),
    path('porno/<int:video_id>/', views.porno_detail, name='porno_detail'),
    path('porno/<int:video_id>/watch/', views.porno_watch, name='porno_watch'),
]
