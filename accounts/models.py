from email.policy import default
from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

# Extending custom User model fields
class User(AbstractUser):
    role=models.CharField(default='user', max_length=50, null=True, blank=True)

