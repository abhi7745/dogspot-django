from django.db import models

from accounts.models import User

# # Create your models here.

class Map_Details(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    email=models.CharField(max_length=255, null=True)
    longitude=models.CharField(max_length=255 ,null=True, blank=True)
    latitude=models.CharField(max_length=255 ,null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True, auto_now_add=False)
    title = models.CharField(max_length=100,null=True, blank=True)
    description = models.CharField(max_length=255,null=True, blank=True)
    no_of_dogs = models.IntegerField(null=True, blank=True)
    behaviour = models.CharField(max_length=255,null=True, blank=True)
    
    def __str__(self):
        return str(self.user)


class Dog_Pics(models.Model):
    map_id = models.ForeignKey(Map_Details, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images')