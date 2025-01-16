from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateListPostAPIView, PostDetailAPIView

urlpatterns = [
    path('api/v1/posts/', CreateListPostAPIView.as_view(), name='get-post-posts'),
    path('api/v1/posts/<int:pk>/', PostDetailAPIView.as_view(), name='get-update-delete-post'),
]