from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    is_passenger = models.BooleanField(default=False)

class driver(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

class passenger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    