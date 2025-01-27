from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from authentication.serializers import RegisterSerializer
from django.http import Http404
from rest_framework import status
from .permissions import IsOwner, IsAuthorOfComment
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .pagination import StandardResultsSetPagination

#Post related Viewset implementing basic CRUD
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH', 'DELETE'):
            return [IsOwner()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
    #POST
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

#Comment related Viewset implementing basic CRUD
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.request.method in ('PUT', 'PATCH', 'DELETE'):
            return [IsAuthorOfComment()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
    #POST
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    #PUT
    def perform_update(self, serializer):
        serializer.save(modified=True)

    #PATCH
    def partial_update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        self.check_object_permissions(request, instance) 
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
