'''
Necesito un programa que haga una operación matemática (por ejemplo 37 +12) y me dé el resultado.

Toda la teoria se encuentra en el primer punto de la Unidad 4 de Google Classroom

Calificación de la actividad

El programa se seguirá ejecutando hasta que yo de la respuesta correcta. (5 puntos)

Si fallo el programa me debe decir si me he pasado o me he quedado corto (2 puntos)

Puedo introducir por pantalla los dos números que quiero que se sumen, por lo tanto la suma ya no es siempre la misma, si no la que el usuario elija. (1 punto)

Aparte de realizar el punto anterior, también podré elegir la operación matemática entre SUMA, RESTA o MULTIPLICACIÓN (2 puntos)
'''

n1=input("introduce un número: ")
n2=input("intoduce otro número: ")
o= input("Elija entre suma, resta, multi : ")
a= int(n1)
b= int(n2)

if (o.lower()=="suma"):
  x= a+b
if (o.lower()=="resta"):
  x= a-b
if (o.lower()=="multi"):
  x= a*b
c= input("Introduce el resultado: ")
while (x != int(c)):
  if(int(c)> x):
    print("El resultado no es correcto, es mayor que el resultado correcto, volver a intentar" )
  else:
    print("El resultado no es correcto, es menor que el resultado correcto, volver a intentar")
  c= input("Introduce el resultado: ")


print("El resultado es correcto")