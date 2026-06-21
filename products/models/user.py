from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.get_full_name()