from django.urls import path, include
from .views import RegisterView

urlpatterns = [
    path('api/v1/token/register/', RegisterView.as_view(), name='register-user'),
]