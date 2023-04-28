import requests
import urllib.request as url
import json
import folium
import datetime
import time

#-------
#APIs
#-------
#Recuperar vuelos para un determinado aeropuerto que llegaron dentro de un intervalo de tiempo dado [comienzo, fin].
#Si no se encuentran vuelos para el período dado, HTTP stats 404 - Not found se devuelve con un cuerpo de respuesta vacío.
# Aviones llegados a Frankfurt International Airport (EDDF) desde 12pm a 1pm en 29 Enero 2018
airport_arrive="https://opensky-network.org/api/flights/arrival?airport=EDDF&begin=1517227200&end=1517230800"

#Recuperar vuelos para un determinado aeropuerto que partieron dentro de un intervalo de tiempo dado [comienzo, fin].
# Aviones que partieron a Frankfurt International Airport (EDDF) desde 12pm a 1pm en 29 Enero 2018
airport_depart="https://opensky-network.org/api/flights/departure?airport=EDDF&begin=1517227200&end=1517230800"

#Esta llamada a la API recupera vuelos durante un determinado intervalo de tiempo [comienzo, fin]
#Vuelos desde 12pm a 1pm en 29 Enero 2018:
flights_time="https://opensky-network.org/api/flights/all?begin=1517227200&end=1517230800"

#Esta llamada API recupera vuelos para un avión en particular dentro de un cierto intervalo de tiempo
#Vuelo D-AIZZ (3c675a) en 29 Enero 2018:
flights_particular="https://opensky-network.org/api/flights/aircraft?icao24=3c675a&begin=1517184000&end=1517270400"

#Esta API nos permite localziar aviones despegados en un área delimitada
#Area delimitada por latitud minima, longitud minima, latitud máxima, longitud máxima
area = "https://opensky-network.org/api/states/all?lamin=39.41&lomin=-3.702&lamax=42.8229&lomax=-2.999"

#Esta API permite detectar varios aviones concretos en tiempo real.
#Avion 3c6444 y 3e1bf9 (siempre con el código icao4)
flight_track="https://opensky-network.org/api/states/all?icao24=3c6444&icao24=3e1bf9"

# Convertir fechas concretas en HORA UNIX
begin_time = datetime.datetime(2021, 7, 26, 21, 20)
end_time = datetime.datetime(2021, 7, 26, 23, 20)

# Imprimo hora estandar
print("Tiempo inicio =>", begin_time)
print("Tiempo Final =>", end_time)

# Convierto e imprimo equivalente en hora UNIX
print("unix_begin_time => ",(time.mktime(begin_time.timetuple())))
print("unix_end_time => ",(time.mktime(end_time.timetuple())))

#Usar la hora actual
presentDate = datetime.datetime.now()
#Convierto a HORA UNIX y guardo en variable
unix_timestamp=time.mktime(presentDate.timetuple())

#Solicitar valores a la API
response_track = url.urlopen(area)
#Leer valores formato JSON
track_data = json.loads(response_track.read())

#Ejemplo de visualización
print(len(track_data["states"]))


