from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom user model to allow for future extension.
    """
    email = models.EmailField(unique=True) # Make email unique

    def __str__(self):
        return self.username