from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]