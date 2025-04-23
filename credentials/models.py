from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=14, primary_key=True)
    password = models.CharField(max_length=30, min_length=10)

    is_superuser = models.BooleanField()