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


    STATE_CHOICE = [
        ("kerala", "Kerala"),
    ]

    DISTRICT_CHOICES = [
        ("thiruvananthapuram", "Thiruvananthapuram"),
        ("kollam", "Kollam"),
        ("pathanamthitta", "Pathanamthitta"),
        ("alappuzha", "Alappuzha"),
        ("kottayam", "Kottayam"),
        ("idukki", "Idukki"),
        ("ernakulam", "Ernakulam"),
        ("thrissur", "Thrissur"),
        ("palakkad", "Palakkad"),
        ("malappuram", "Malappuram"),
        ("kozhikode", "Kozhikode"),
        ("wayanad", "Wayanad"),
        ("kannur", "Kannur"),
        ("kasaragod", "Kasaragod"),
    ]

    role=models.CharField(default='user', choices=ROLE_CHOICE, max_length=50, null=True, blank=True)
    status=models.CharField(default='active', choices=STATUS_CHOICE, max_length=50, null=True, blank=True)
    profile_pic=models.ImageField(upload_to='users/profile_pic', default="default_profile_pic.png", null=True, blank=True)
    latitude=models.CharField(max_length=255, null=True, blank=True)
    longitude=models.CharField(max_length=255, null=True, blank=True)
    state=models.CharField(max_length=255, choices=STATUS_CHOICE, null=True, blank=True)
    district=models.CharField(max_length=255, choices=DISTRICT_CHOICES, null=True, blank=True)
    place=models.CharField(max_length=255, null=True, blank=True)