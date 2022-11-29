from django.shortcuts import render

import folium
from folium import plugins

import geocoder

# Create your views here.

def dashboard(request):
    return render(request, 'admin/dashboard.html')


def users(request):
    return render(request, 'admin/users.html')


def map(request):
    state = geocoder.osm('Kumaranalloor, Kottayam, Kottayam, Kerala, India')
    map1  = folium.Map(location=[state.lat, state.lng], zoom_start=13)

    plugins.Fullscreen(position='topright').add_to(map1)

    # data = [[19, 12, 3000], [20,10,4999]]
    # data = [[19, state.lat, 3000], [20, state.lng, 4999]]
    # plugins.HeatMap(data).add_to(map1)

    data = [[9.6174363, 76.5327349], [9.618650, 76.509079], [9.670300, 76.556763], [9.718096, 76.544586], [9.63375, 76.52090]]

    for x in data:
        print(x)


        folium.Marker(
            x, 
            popup="<h1 style='text-align:center;'>Kumaranallor<br><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGtuJgv57yb7bUXsCri1_tKp_Q372TXmWlFTShxcz_&s' /><br><a href='https://www.w3schools.com' target='_blank'>Visit</a></h1>",
            tooltip='Kumaranalloor',
            icon=folium.Icon(color="green")

        ).add_to(map1)
    
    # folium.Marker(
    #     [9.618650, 76.509079], 
    #     popup="<h1 style='text-align:center;'>Kumaranallor<br><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGtuJgv57yb7bUXsCri1_tKp_Q372TXmWlFTShxcz_&s' /><br><a href='https://www.w3schools.com'>Visit</a></h1>",
    #     tooltip='Kumaranalloor',
    #     icon=folium.Icon(color="red", icon="info-sign"),

    # ).add_to(map1)


    map1.add_child(folium.ClickForMarker(popup=f"<a href='https://www.w3schools.com' target='_blank'>Add Dogspot</a>"))
    # map1.add_child(folium.ClickForMarker(popup=None))

    # map1.get_root().html.add_child(folium.Element('''
    # <div>
    #     <h1>Hello world</h1>
    # </div>
    # '''))

    print(map1.location, 'aaaaaaaaaaaaaaaa')

    map1 = map1._repr_html_()
    print(state.lat)
    print(state.lng)


    return render(request, 'admin/map.html', {'map': map1})