from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_photo = models.ImageField(upload_to="profile_photo/", blank=True, default='1')
