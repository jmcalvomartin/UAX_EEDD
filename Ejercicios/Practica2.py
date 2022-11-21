'''
Ejercicio 1
Realiza un programa que introduzcas por pantalla dos números y te diga cual es el mayor o si son iguales
Complica el ejercicio introduciendo 3 números
'''

a= int(input("Dime un número: "))
b= int(input("Dime otro número: "))
c= int(input("Dime un tercer número: "))

if a>b:
  if a>c:
    print("El mayor es: ",a)
  else:
    print("El mayor es:",c)


else:
  if b>c:
    print("El mayor es:",b)
  else: print("El mayor es:",c)


'''
Ejercicio 2 (tu primer algoritmo)
Realiza un programa que al introducir un número te diga si es par o impar (cualquier número)
'''

a=int(input("Introduce un número: "))
if (a%2 == 0):
  print(a," es par ")
else:
  print (a," es impar")