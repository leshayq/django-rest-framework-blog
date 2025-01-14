from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)