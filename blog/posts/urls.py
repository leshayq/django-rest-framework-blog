from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreateListPostAPIView, PostDetailAPIView, CreateListCommentAPIView, CommentDetailAPIView

urlpatterns = [
    path('api/v1/posts/', CreateListPostAPIView.as_view(), name='get-post-posts'),
    path('api/v1/posts/<int:pk>/', PostDetailAPIView.as_view(), name='get-update-delete-post'),

    path('api/v1/comments/', CreateListCommentAPIView.as_view(), name='get-post-comments'),
    path('api/v1/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='get-update-delete-comment'),
]