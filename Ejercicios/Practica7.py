#P7
import random
import time

#Guardo fichero de datos
filename= "Data/cities.txt"
#Lo abro en formato UTF-8
file = open(filename, encoding="utf8")
#Convierto cada ciudad en un elemntod e la lista
lista =file.read().splitlines()

print("Número de ciudades: ",len(lista))

#Imprimimos las 10 primeras ciudades con sus respectivos códigos de ticket
print(lista[1:10])