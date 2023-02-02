

def ordenar(lista):
    for i in range (len(lista)):
        ultimo=len(lista)-1
        while ultimo >= i:
            if lista[ultimo]< lista[ultimo-1]:
                temp=lista[ultimo]
                lista[ultimo]=lista[ultimo-1]
                lista[ultimo-1]=temp

            ultimo-=1

    return lista


#Recursividad
def ordenar_r(lista,n):
    if (n<=1):
        return lista
    for x in range (0, n-1):
        if lista[x] > lista[x+1]:
            temp=lista[x]
            lista[x]=lista[x+1]
            lista[x+1]=temp

    ordenar_r(lista,n-1)
    return lista


import random
import time

lista=random.sample(range(0,999),999)

inicio=time.time()
ordenar(lista)
fin=time.time()
print(fin-inicio)

inicio=time.time()
n=len(lista)
ordenar_r(lista,n)
fin=time.time()
print(fin-inicio)