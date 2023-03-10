#Geolocalización Python
import geopy.geocoders as geo
import folium

gps=geo.Nominatim(user_agent="MyGeo")

class Mapa:
    def __init__(self,lugar):
        self.lugar=lugar
        loc = gps.geocode(lugar)
        self.m=folium.Map([loc.latitude,loc.longitude],
                          tiles="Stamen Terrain",zoom_start=5)

    def guardar(self,name):
        self.name=name
        self.m.save(self.name+".html")

    def marcador(self,marca,color):
        self.marca=marca
        self.color=color
        loc = gps.geocode(marca)
        folium.Marker([loc.latitude,loc.longitude],popup="Pueblo",
                      tooltip="Aquí",
                      icon=folium.Icon(icon="cloud",color=self.color)).add_to(self.m)

    def zona(self,circulo):
        self.circulo=circulo
        loc = gps.geocode(circulo)
        folium.CircleMarker([loc.latitude,loc.longitude],
                            radius=50,
                            popup="Zona Prohibida",
                            color="#3186cc",
                            fill=True,
                            fill_color="#3186cc").add_to(self.m)
    def marcas_on(self):
        self.m.add_child(folium.LatLngPopup())
        self.m.add_child(folium.ClickForMarker(popup="Mis Marcas"))

    def rutas(self,origen,destino):
        self.origen=origen
        self.destino=destino
        loc_o = gps.geocode(self.origen)
        loc_d = gps.geocode(self.destino)
        folium.PolyLine([(loc_o.latitude,loc_o.longitude),(loc_d.latitude,loc_d.longitude)],
        color="red").add_to(self.m)



spain=Mapa("Toledo")
spain.marcador("Fuensalida","red")
spain.zona("Torrijos")
#spain.marcas_on()
spain.rutas("Sonseca","Madrid")
spain.guardar("spain")
