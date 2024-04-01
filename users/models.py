from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=100)
    # password = models.CharField(max_length=100)
    python = models.IntegerField(default=0)
    java = models.IntegerField(default=0)
    javaScript = models.IntegerField(default=0)

    def __str__(self):
        return self.username
