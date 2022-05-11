from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
<<<<<<< HEAD
    profile_photo = models.ImageField(upload_to='profile_photo/', blank=True, default='1')
=======
    profile_photo = models.ImageField(upload_to="profile_photo/", blank=True, default='1')
>>>>>>> 1ac6e7e5c274fd1b6a1aac2f2b03ee985fe79e7d
