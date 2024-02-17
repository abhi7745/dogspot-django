from django.shortcuts import render, redirect

from user.models import Map_Details, Dog_Pics
from django.contrib import messages

from django.http import JsonResponse


import geocoder # for getting map location(latitude, longitude)

from accounts.models import User


# Create your views here.


# dashboard

def dashboard(request):
    user_count = User.objects.exclude(role = 'admin').count()

    print(user_count, 'testing')
    context = {'user_count': user_count}
    return render(request, 'user/dashboard.html', context)

# show all dogspot marker in map
def map_view(request):
    latlng = geocoder.ip('me')
    # if request.user.is_authenticated: 
    #     print(request.user,'User already logged in')
    #     return render(request,'admin/dashboard.html')
    # else:
    print(latlng)
    print(latlng.ip)
    print(latlng.lat)
    print(latlng.lng)
    return render(request, 'user/map_view.html',{'lat':latlng.lat, 'lng':latlng.lng})


def static_dogspot_marker_map(request):
    latlng = geocoder.ip('me')
    # if request.user.is_authenticated: 
    #     print(request.user,'User already logged in')
    #     return render(request,'admin/dashboard.html')
    # else:
    print(latlng)
    print(latlng.ip)
    print(latlng.lat)
    print(latlng.lng)
    return render(request, 'user/static_dogspot_marker_map.html', {'lat':latlng.lat, 'lng':latlng.lng})


def add_dogspot(request, lat, lng):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')
        no_of_dogs = request.POST.get('no_of_dogs')
        behaviour = request.POST.get('behaviour')
        # images = request.FILES.getlist('images1')

        print('title', title)
        print('description', description)
        print('no_of_dogs', no_of_dogs)
        print('behaviour', behaviour)
        

        if not Map_Details.objects.filter(latitude=lat,longitude=lng).exists():
            map_obj = Map_Details.objects.create(
                email = request.user.username,
                user = request.user,
                title = title,
                description = description,
                no_of_dogs = no_of_dogs,
                behaviour = behaviour,
                longitude =lng,
                latitude = lat
            )
            print('map details point created successfully')

            for file_num in range(0, int(length)):
                image = request.FILES.get(f'images{file_num}')
                print('image : ', image)
                Dog_Pics.objects.create(
                    map_id = map_obj,
                    image = image
                )
                print('image db created created')

        else:
            # messages.error(request, 'Map Location already added by other user', extra_tags='map_point_already_exist_error')
            print('Map Location already added by other user')
            return JsonResponse({'point_exist': True},safe=False)

    print(request.user, 'usertttttttttttt')

    return render(request, 'user/add_dogspot.html', {'lat':lat, 'lng':lng})

def dogspot_list(request):
    map_data = Map_Details.objects.filter(user=request.user.id)
    # print(map_data, request.user.role)
    context = {'map_data' : map_data }
    return render(request, 'user/dogspot_list.html', context)

# update
# delete

def all_dogspot_list(request):
    return render(request, 'user/all_dogspot_list.html')


def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):
    return render(request, 'user/profile_update.html')


def settings(request):
    return render(request, 'user/profile.html')