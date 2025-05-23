from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager


class Vault_User(AbstractBaseUser):
    username = models.TextField(max_length=14, primary_key=True)
    password = models.TextField(max_length=30)
    user_first_name = models.TextField(max_length=30, default="")
    user_last_name = models.TextField(max_length=50, default="")
    USERNAME_FIELD = 'username' 

    is_superuser = models.BooleanField()

    REQUIRED_FIELDS = ['user_first_name', 'user_last_name', 'password', username] 
    objects = BaseUserManager()
    
    def return_full_name(self):
        return f"{self.user_first_name} {self.user_last_name}"
    
    def return_username(self):
        return self.username

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def __str__(self):
        return self.username


class Credential(models.Model):
    name = models.TextField(max_length=20, primary_key=True)
    website = models.TextField(max_length=20)
    username = models.TextField(max_length=20)
    password = models.TextField(max_length=20)
    notes = models.TextField(max_length=100)

    def return_name(self):
        return self.name
    
    def return_website(self):
        return self.website
    
    def return_username(self):
        return self.username
    
    def return_password(self):
        return self.password
    
    def return_notes(self):
        return self.notes

    def __str__(self):
        return self.website
    

