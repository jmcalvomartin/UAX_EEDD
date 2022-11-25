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
lista = [random.randint(0,100) for x in range(20)]
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
lista = [random.randint(0,100) for x in range(20)]
print(lista)
lista2=[]
while len(lista)>0:
  max=lista[0]
  for x in range(1,len(lista)):
    if lista[x]>max:
      max=lista[x]
  lista2.append(max)
  lista.remove(max)
print(lista2)
