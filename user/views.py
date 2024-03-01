from django.shortcuts import render, redirect

from user.models import Map_Details, Dog_Pics
from django.contrib import messages

from django.http import JsonResponse, HttpRequest, HttpResponse


import geocoder # for getting map location(latitude, longitude)

from accounts.models import User

import os

from PIL import Image # for image compression
from io import BytesIO # for image compression

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

    map_db = Map_Details.objects.all()
    
    context = {'lat':latlng.lat, 'lng':latlng.lng, 'map_db' : map_db}
    return render(request, 'user/map_view.html', context)


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
    map_db = Map_Details.objects.all()
    context = {'lat':latlng.lat, 'lng':latlng.lng, 'map_db' : map_db}
    return render(request, 'user/static_dogspot_marker_map.html', context)



from PIL import Image # for image compression
from io import BytesIO # for image compression
from django.core.files.base import ContentFile #for image compression
# image compression function
def image_compressor(image_file, quality=90):
    # Open the image using PIL
    img = Image.open(image_file)
    print(f'image name: {image_file} is compressing.........')

    # Resize the image (optional, if you want to resize)
    width, height = img.size
    img = img.resize((width, height), Image.ANTIALIAS)

    # Convert image to bytes with compression quality
    img_bytes = BytesIO()
    img.save(img_bytes, format='JPEG', quality=quality)

    # Reset the file pointer to the beginning
    img_bytes.seek(0)

    # Create a ContentFile object from the compressed image data
    compressed_image = ContentFile(img_bytes.read(), name=image_file.name)

    return compressed_image # ready for saving to database in "ImageField" field


def add_dogspot(request, lat, lng):
    if request.method == 'POST':
        length = request.POST.get('length')
        place_name = request.POST.get('place_name')
        description = request.POST.get('description')
        no_of_dogs = request.POST.get('no_of_dogs')
        behaviour = request.POST.get('behaviour')
        km = request.POST.get('km')
        # images = request.FILES.getlist('images1')

        print('place_name', place_name)
        print('description', description)
        print('no_of_dogs', no_of_dogs)
        print('behaviour', behaviour)
        print('km:', km)

        #  Aggressive, Biting, Social, Friendly, Barking, Chasing, Territorial, Illness 
        zone = {}
        # Red Zone (Aggressive, Biting, Territorial, Illness):
        if 'Aggressive' in behaviour or 'Biting' in behaviour or 'Territorial' in behaviour or 'Illness' in behaviour:
            print( 'Red Zone (Aggressive, Biting, Territorial, Illness):..................')

            zone['zone'] = 'red'
            zone['radius_color'] = '#FF0000'
            zone['radius_color_hexcode'] = '#FF0000'

        # Yellow Zone (Barking, Chasing):
        elif 'Barking' in behaviour or 'Chasing' in behaviour:
            print('Yellow Zone (Barking, Chasing):..................')

            zone['zone'] = 'yellow'
            zone['radius_color'] = '#FFD326'
            zone['radius_color_hexcode'] = '#FFD326'

        # Green Zone (Social, Friendly)
        else:
            print(' Green Zone (Social, Friendly)..................')

            zone['zone'] = 'green'
            zone['radius_color'] = '#2AAD27'
            zone['radius_color_hexcode'] = '#2AAD27'

        print('Zone dictionary:', zone)
        print('Zone:', zone['zone'])
        print('radius_color:', zone['radius_color'])
        print('radius_color_hexcode:', zone['radius_color_hexcode'])
        

        if not Map_Details.objects.filter(latitude=lat,longitude=lng).exists():
            map_obj = Map_Details.objects.create(
                email = request.user.username,
                user = request.user,
                place_name = place_name,
                description = description,
                no_of_dogs = no_of_dogs,
                behaviour = behaviour,
                longitude = lng,
                latitude = lat,
                zone = zone['zone'],
                radius_color=zone['radius_color'],
                radius_color_hexcode=zone['radius_color_hexcode'],
                km_distance=km
            )
            print('map details point created successfully')

            for file_num in range(0, int(length)):
                image = request.FILES.get(f'images{file_num}')
                print('image : ', image)
                Dog_Pics.objects.create(
                    map_id = map_obj,
                    # image = image
                    image = image_compressor(image) # calling a image compression function
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
def dogspot_update(request):
    if request.method == 'POST' and not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        object_id = request.POST.get('id')
        print(object_id, 'object_id')

        if Map_Details.objects.filter(user=request.user.id, id=object_id).exists():
            single_map_object = Map_Details.objects.filter(user=request.user.id, id=object_id).first()
            print(single_map_object.id, single_map_object.place_name)

            context = {'single_map_object' : single_map_object}
            return render(request, 'user/dogspot_update.html', context)


    # def is_ajax(request):
    #     return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    # if request.is_ajax():
    # if is_ajax(request=request):
    # if HttpRequest.is_ajax()
        
    # if isinstance(request, HttpRequest) and request.headers.get('x-requested-with') == 'XMLHttpRequest':
    
    # ajax form area
    elif request.headers.get('x-requested-with') == 'XMLHttpRequest':
        object_id = request.POST.get('id')
        length = request.POST.get('length')
        place_name = request.POST.get('place_name')
        description = request.POST.get('description')
        no_of_dogs = request.POST.get('no_of_dogs')
        behaviour = request.POST.get('behaviour')
        # images = request.FILES.getlist('images1')
        km = request.POST.get('km')

        print(object_id, 'object_id')
        print('place_name', place_name)
        print('description', description)
        print('no_of_dogs', no_of_dogs)
        print('behaviour', behaviour)
        print('km:', km)


        if Map_Details.objects.filter(user=request.user.id, id=object_id).exists():
            map_object = Map_Details.objects.get(user=request.user.id, id=object_id)


            zone = {}
            # Red Zone (Aggressive, Biting, Territorial, Illness):
            if 'Aggressive' in behaviour or 'Biting' in behaviour or 'Territorial' in behaviour or 'Illness' in behaviour:
                print( 'Red Zone (Aggressive, Biting, Territorial, Illness):..................')

                zone['zone'] = 'red'
                zone['radius_color'] = '#FF0000'
                zone['radius_color_hexcode'] = '#FF0000'

            # Yellow Zone (Barking, Chasing):
            elif 'Barking' in behaviour or 'Chasing' in behaviour:
                print('Yellow Zone (Barking, Chasing):..................')

                zone['zone'] = 'yellow'
                zone['radius_color'] = '#FFD326'
                zone['radius_color_hexcode'] = '#FFD326'

            # Green Zone (Social, Friendly)
            else:
                print(' Green Zone (Social, Friendly)..................')

                zone['zone'] = 'green'
                zone['radius_color'] = '#2AAD27'
                zone['radius_color_hexcode'] = '#2AAD27'

            print('Zone dictionary:', zone)
            print('Zone:', zone['zone'])
            print('radius_color:', zone['radius_color'])
            print('radius_color_hexcode:', zone['radius_color_hexcode'])

            map_object.place_name = place_name
            map_object.description = description
            map_object.no_of_dogs = no_of_dogs
            map_object.behaviour = behaviour
            map_object.zone = zone['zone']
            map_object.radius_color=zone['radius_color']
            map_object.radius_color_hexcode=zone['radius_color_hexcode']
            map_object.km_distance=km

            map_object.save() # re-saving old data with new data


            dog_pics_db = map_object.dog_pics_set.all() # all child images of "Map_Details" table (reverse relationship) 

            dog_pics_db_images_length = dog_pics_db.count() # all images count(length)

            print('count :', dog_pics_db_images_length)
            print('length :' , length)



            # only check if new image found
            # condition for checking new image comes from "form" or not
            if dog_pics_db_images_length == 1 or dog_pics_db_images_length != int(length):
                print('changes detected ...............................')

                # deleting all "old-images" from media folder
                for dog_pics_row in map_object.dog_pics_set.all():

                    if len(request.FILES) != 0:
                        if dog_pics_row.image and os.path.exists(dog_pics_row.image.path):
                            os.remove(dog_pics_row.image.path) # removing the "old-image" from media folder
                            print('old image removed')

            
                dog_pics_db.delete() # deleting all image url objects from database "image" field


                # adding new "image urls" to database and "image files" to media folder
                for file_num in range(0, int(length)):
                    image = request.FILES.get(f'images{file_num}')
                    print('image : ', image, 'form image value')

                    # adding images to database and media folder
                    Dog_Pics.objects.create(
                        map_id = map_object,
                        # image = image
                        image = image_compressor(image) # calling a image compression function
                    )
                    print('image db again created')


            else:
                print('no image change detected...............................')

            # for dog_pics_row in map_object.dog_pics_set.all():
            #     print(dog_pics_row.image.name.split('/')[-1], 'database value')        

        return JsonResponse({'status': True},safe=False)

    else:
        return redirect(dogspot_list)


def dogspot_delete(request):
    if request.method == 'POST':
        object_id = request.POST.get('delete_id')
        if Map_Details.objects.filter(user=request.user.id, id=object_id).exists():
            map_object = Map_Details.objects.get(user=request.user.id, id=object_id)

            print('Place Name:', map_object.place_name)


            dog_pics_db = map_object.dog_pics_set.all() # all child images of "Map_Details" table (reverse relationship)

            # deleting all "old-images" from media folder
            for dog_pics_row in dog_pics_db:

                # if len(request.FILES) != 0:
                if dog_pics_row.image and os.path.exists(dog_pics_row.image.path):
                    os.remove(dog_pics_row.image.path) # removing the "old-image" from media folder
                    print('old image removed')

            messages.success(request, map_object.place_name , extra_tags='delete_msg')
        
            dog_pics_db.delete() # deleting all image url objects from database
            print('All Dog_pics db deleted sucessfully')
            map_object.delete() # deleting map object form database
            print('Map_Details db deleted sucessfully')


            return redirect('user.dogspot_list')
    
        else:
            return redirect('user.dashboard')
    
    else:
        return redirect('user.dashboard')


def all_dogspot_list(request):
    return render(request, 'user/all_dogspot_list.html')


def profile(request):
    return render(request, 'user/profile.html')

def profile_update(request):
    return render(request, 'user/profile_update.html')


def settings(request):
    return render(request, 'user/profile.html')