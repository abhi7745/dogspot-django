from django.shortcuts import render

import geocoder

from user.models import Map_Details
# Create your views here.

# index
def index(request):
    latlng = geocoder.ip('me')
    # if request.user.is_authenticated: 
    #     print(request.user,'User already logged in')
    #     return render(request,'admin/dashboard.html')
    # else:
    print(latlng)
    print(latlng.ip)
    print(latlng.lat)
    print(latlng.lng)

    map_db = Map_Details.objects.all()
    return render(request,'home/home.html',{'lat':latlng.lat, 'lng':latlng.lng, 'map_db': map_db})



# map for listing all dog spots
def map(request):
    latlng = geocoder.ip('me')

    map_db = Map_Details.objects.all()
    context = {'map_db': map_db, 'lat':latlng.lat, 'lng':latlng.lng}
    return render(request, 'home/map.html', context)


def donation(request):
    context = {}
    return render(request, 'home/donation.html', context)