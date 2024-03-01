from django.db import models

from accounts.models import User

from PIL import Image # for image compression

# # Create your models here.

class Map_Details(models.Model):
  
    ZONE_COLORS = [
        ('red', 'Red'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
    ]
    
    RADIUS_COLORS = [
        ('#FF0000', 'Red'),
        ('#FFD326', 'Yellow'),
        ('#2AAD27', 'Green'),
    ]

    KM_DISTANCE = [
        ('250', '500 Meters'),
        ('500', '1 Km'),
        ('1000', '2 Km'),
        ('1500', '3 Km'),
        ('2000', '4 Km'),
        ('2500', '5 Km'),
    ]

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    email=models.CharField(max_length=255, null=True)
    longitude=models.CharField(max_length=255 ,null=True, blank=True)
    latitude=models.CharField(max_length=255 ,null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True, auto_now_add=False)
    place_name = models.CharField(max_length=100,null=True, blank=True)
    description = models.CharField(max_length=255,null=True, blank=True)
    no_of_dogs = models.IntegerField(null=True, blank=True)
    behaviour = models.CharField(max_length=255,null=True, blank=True)
    zone = models.CharField(max_length=50,choices=ZONE_COLORS)
    radius_color = models.CharField(max_length=50, choices=RADIUS_COLORS)
    radius_color_hexcode = models.CharField(max_length=50, choices=RADIUS_COLORS)
    km_distance = models.IntegerField(choices=KM_DISTANCE)
    
    def __str__(self):
        return str(self.user)


class Dog_Pics(models.Model):
    map_id = models.ForeignKey(Map_Details, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images')