from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=11)
    avatar = models.ImageField(upload_to='icon',default='icon/default.png')