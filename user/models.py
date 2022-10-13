from django.db import models

from accounts.models import User

# # Create your models here.

class User_Account(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    email=models.CharField(max_length=255, null=True)
    longitude=models.CharField(max_length=255 ,null=True, blank=True)
    latitude=models.CharField(max_length=255 ,null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return str(self.user)


class Dog_Pics(models.Model):
    user_account = models.ForeignKey(User_Account, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images')