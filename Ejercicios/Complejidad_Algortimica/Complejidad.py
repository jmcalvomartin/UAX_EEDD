'''
Complejidad de los Algoritmos
Un algoritmo implica la descripción precisa de los pasos a seguir para alcanzar la solución de un problema dado.
La teoría de complejidad computacional estudia y clasifica los algoritmos y problemas computacionales en función de su coste y dificultad de resolver.

Para representar la unidad de medible de complejidad se usa O(orden)

Tipos de complejidad

O(1): Constante
Un programa que me diga si un número es par o impar
'''

num=int(input("Dime un número: "))
if num%2==0:
  print("Par")
else: print("Impar")

'''
O(n): Lineal
Un programa que me diga el número más alto de una lista
'''
import random
lista = [random.randint(0,10000) for x in range(2000)]
print(lista)

max=lista[0]
for x in range(1,len(lista)):
  if lista[x]>max:
    max=lista[x]
print(max)

'''
O(n^2): Cuadrático
Un programa que ordena una lista dada
'''
import random
import time
#lista = [random.randint(0,10000) for x in range(10000)]
lista=random.sample(range(0,50),10)
print(lista)
lista2=[]

inicio=time.time()
while len(lista)>0:
  max=lista[0]
  for x in range(1,len(lista)):
    if lista[x]<max:
      max=lista[x]
  lista2.append(max)
  lista.remove(max)
print(lista2)
fin=time.time()
print("Tiempo de ejecución ",fin-inicio)

'''
Complejidad a^n
'''
escaleras=2
pisos=200

for x in range(0,pisos):
  print("El número de salidas es ", escaleras**x)

'''
Algoritmos de búsqueda
'''
import random
import time
#lista = [random.randint(0,10000) for x in range(10000)]
lista=random.sample(range(0,10000000000),800000)
lista.sort()
#print(lista)

search=int(input("Dime número a buscar: "))
inicio=time.time()
for x in range (0,len(lista)):
  if search==lista[x]:
    print("La posición es ", x)
    break
fin=time.time()
print("Tiempo algortimo de búsqueda tradicional ",fin-inicio)

#Algortimo Binario
primero=0
ultimo=len(lista)-1
mitad=0

inicio=time.time()
while primero <= ultimo:
  mitad =(ultimo + primero) // 2
  if lista[mitad]<search:
    primero= mitad + 1
  elif lista[mitad]>search:
    ultimo =mitad -1
  else:
    print("Elemento en posición ", mitad)
    break
fin=time.time()
print("Tiempo algortimo de búsqueda binaria ",fin-inicio)