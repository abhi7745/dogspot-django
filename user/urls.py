from django.urls import path

from user.views import *

urlpatterns = [
    path('dashboard/', dashboard, name='user.dashboard'),
    path('map-view/', map_view, name='user.map_view'),
    path('map-maker/', static_dogspot_marker_map, name='user.static_dogspot_marker_map'),
    path('add-dogspot/<str:lat>/<str:lng>/', add_dogspot, name='user.add_dogspot'),
    path('dogspot_list/', dogspot_list, name='user.dogspot_list'),
    path('dogspot_update/', dogspot_update, name='user.dogspot_update'),
    path('dogspot_delete/', dogspot_delete, name='user.dogspot_delete'),
]