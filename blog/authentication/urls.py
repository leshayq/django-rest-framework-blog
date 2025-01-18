from django.urls import path, include
from .views import UserListCreateAPIView, UserDetailAPIVIew

urlpatterns = [
    path('api/v1/users/', UserListCreateAPIView.as_view(), name='get-post-users'),
    path('api/v1/users/<int:pk>/', UserDetailAPIVIew.as_view(), name='get-user'),
]