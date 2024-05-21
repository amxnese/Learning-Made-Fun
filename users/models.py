from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
class CustomUser(AbstractUser):
    python = models.IntegerField(default=0)
    java = models.IntegerField(default=0)
    javaScript = models.IntegerField(default=0)
    profile_picture = models.ImageField(null=True, blank=True, upload_to='', default='')

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return f"Comment by {self.user.username} on {self.created_at}"
