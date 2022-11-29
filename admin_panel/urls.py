from django.urls import path

from admin_panel.views import *

urlpatterns = [
    path('dashboard/', dashboard, name='admin.dashboard'),
    path('map/', map, name='admin.map'),
]