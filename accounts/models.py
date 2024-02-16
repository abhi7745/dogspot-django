from email.policy import default
from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

# Extending custom User model fields
class User(AbstractUser):
    ROLE_CHOICE = [
        ("admin", "admin"),
        ("user", "user")
    ]
    STATUS_CHOICE = [
        ("active", "active"),
        ("suspend", "suspend"),
        ("ban", "ban")
    ]
    role=models.CharField(default='user', choices=ROLE_CHOICE, max_length=50, null=True, blank=True)
    status=models.CharField(default='active', choices=STATUS_CHOICE, max_length=50, null=True, blank=True)
    place=models.CharField(max_length=255, null=True, blank=True)
    latitude=models.CharField(max_length=255, null=True, blank=True)
    longitude=models.CharField(max_length=255, null=True, blank=True)
