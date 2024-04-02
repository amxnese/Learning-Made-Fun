from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    python = models.IntegerField(default=0)
    java = models.IntegerField(default=0)
    javaScript = models.IntegerField(default=0)
