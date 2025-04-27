from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Vault_User(models.Model):
    username = models.CharField(max_length=14, primary_key=True)
    password = models.CharField(max_length=30)
    user_first_name = models.CharField(max_length=30, default="")
    user_last_name = models.CharField(max_length=30, default="")

    is_superuser = models.BooleanField()


class Credential(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    website = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    notes = models.TextField(max_length=100)

    def __str__(self):
        return self.website
