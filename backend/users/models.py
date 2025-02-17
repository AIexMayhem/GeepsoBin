from django.contrib.auth.models import User
from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)