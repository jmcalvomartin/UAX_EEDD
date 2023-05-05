import folium as fl
from folium.plugins import MarkerCluster, HeatMap, Fullscreen, MiniMap, HeatMapWithTime, FloatImage, LocateControl , MeasureControl
import geopy.geocoders as geo
import geopy.distance as dist
calle = (41.6569033, -4.6990056)
catedral = (42.59944444, -5.56666667)
print(dist.geodesic(calle, catedral).kilometers)

gps=geo.Nominatim(user_agent="MyGeo")

loc=gps.geocode("Madrid")
print(loc.latitude, loc.longitude)


class Mapa:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.m=fl.Map(location=[self.x,self.y],tiles="Stamen Terrain",zoom_start=8)
    def save(self,name):
        self.name=name
        self.m.save(self.name+".html")

    def marcador(self,mx,my):
        self.mx=mx
        self.my=my
        fl.Marker([self.mx,self.my], popup="Lugar", tooltip="Aquí", icon=fl.Icon(icon="cloud",color="green")).add_to(self.m)

    def circulo(self,cx,cy):
        self.cx = cx
        self.cy = cy
        fl.CircleMarker([self.cx, self.cy],radius=50,popup="Laurelhurst Park",color="#3186cc",fill=True,fill_color="#3186cc",).add_to(self.m)

    def marcas_on(self):
        self.m.add_child(fl.ClickForMarker(popup="Mis puntos"))
        self.m.add_child(fl.LatLngPopup())

    def linea(self):
        self.coordenadas=[(self.mx,self.my),(self.cx,self.cy)]
        fl.PolyLine(self.coordenadas,tooltip="Carretera",color="red").add_to(self.m)

    def Pantalla(self):
        Fullscreen(position='topleft', title='Full Screen', title_cancel='Exit Full Screen', force_separate_button=False).add_to(self.m)

    def Minimap(self):
        MiniMap(tile_layer=None, position='bottomright', width=150, height=150, collapsed_width=25, collapsed_height=25, zoom_level_offset=-5, zoom_level_fixed=None, center_fixed=False, zoom_animation=False, toggle_display=False, auto_toggle_display=False, minimized=False).add_to(self.m)

    def Medidas(self):
        MeasureControl(position='topright', primary_length_unit='meters', secondary_length_unit='miles').add_to(self.m)
    #LocateControl(auto_start=False).add_to(mapa)

eeuu=Mapa(40.4167047,-3.7035825)
eeuu.marcador(45.8,-121)
eeuu.circulo(44.9,-124)
eeuu.linea()
eeuu.Minimap()
eeuu.Pantalla()
eeuu.Medidas()
#eeuu.marcas_on()
eeuu.save("eeuu")

import urllib.request as url
import json

ISS = url.Request("http://api.open-notify.org/iss-now.json")
response_ISS = url.urlopen(ISS)

ISS_data = json.loads(response_ISS.read())

print (ISS_data['iss_position']['latitude'])
print (ISS_data['iss_position']['longitude'])

latitude=ISS_data['iss_position']['latitude']
longitude=ISS_data['iss_position']['longitude']

Astros=url.Request("http://api.open-notify.org/astros.json")
response_astros = url.urlopen(Astros)
Astros_data = json.loads(response_astros.read())
print(Astros_data["people"])

for x in range (len(Astros_data["people"])):
    print (Astros_data["people"][x]["name"])

iss=Mapa(latitude,longitude)
iss.marcador(latitude,longitude)
iss.save("iss")

