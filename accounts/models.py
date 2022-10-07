# This Django app is build for automation using python, build by Abhijith KR 

from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class User_Account(models.Model):
    user_id=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email=models.CharField(max_length=255,null=True)