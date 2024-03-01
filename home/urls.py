from django.urls import path

from home.views import *

urlpatterns = [
    path('', index, name='home.index'),
    path('map', map, name='home.map'),
    path('donation', donation, name='home.donation'),
]