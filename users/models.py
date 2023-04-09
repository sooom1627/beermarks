from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    upic = models.ImageField(upload_to="upic/", null = True, height_field=None, width_field=None, max_length=None, default="upic/default-user.png")
    udesc = models.CharField(max_length=225, null=True, blank=True)
    uname = models.CharField(max_length=50, default="noname", blank=True)