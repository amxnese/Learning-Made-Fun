from django.db import models

class Member(models.Model):
  username = models.CharField(max_length=100)
  password = models.CharField(max_length=200)
  python = models.IntegerField(default=0)
  java = models.IntegerField(default=0)
  javaScript = models.IntegerField(default=0)

  def __str__(self):
    return self.username