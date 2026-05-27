from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_image = models.ImageField(
        "profile image", upload_to="users/profile", blank=True
    )
    short_description = models.TextField("bio", blank=True)