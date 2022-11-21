'''
Nos encontramos en el departamento de recursos humanos de un colegio y necesitamos un programa que nos diga si podemos contratar a un porfesor o profesora con las siguientes características, es decir que sea profesor y hable uno de esos dos idiomas culaquier otra opción no será contratado

Necesitamos que hable Inglés o Francés
Debes pedir como variables la profesión y el idioma.
Se debe usar and y or, y el programa unicamente debe contener un solo IF
'''

idioma= input("introduce que idioma hablas aparte de español: ")
profesion= input("introduce tu profesión: ")

if(idioma== "inglés" or idioma== "francés") and (profesion=="profesor"):
  print("Enhorabuena, estas contratado")
else:
  print("Lo siento, no estas contratado")


'''
Ejercicio 2
En este ejercicio necesito un programa que me pida mi número de DNI SIN LETRA y me devuelva el número del DNI con la letra adecuada a mi documento.

Aunque pueda parecer extraño debemos saber que la letra del DNI, NIF o NIE es fácilmente calculable a partir de los números. 
Esto se debe a que la letra del DNI se calcula a través del algoritmo 23. 
Para ayudaros con este ejercicio tenéis esta web: https://www.serautonomo.net/como-calcular-la-letra-del-dni.html
'''
DNI=input("introduce tu DNI sin letra:" )
a = int(DNI)
if (a%23==0):
  print("Tu letra es T")
if (a%23==1):
  print("Tu letra es R")
if (a%23==2):
  print("Tu letra es W")
if (a%23==3):
  print("Tu letra es A")
if (a%23==4):
  print("Tu letra es G")
if (a%23==5):
  print("Tu letra es M")
if (a%23==6):
  print("Tu letra es Y")
if (a%23==7):
  print("Tu letra es F")
if (a%23==8):
  print("Tu letra es P")
if (a%23==9):
  print("Tu letra es D")
if (a%23==10):
  print("Tu letra es X")
if (a%23==11):
  print("Tu letra es B")
if (a%23==12):
  print("Tu letra es N")
if (a%23==13):
  print("Tu letra es J")
if (a%23==14):
  print("Tu letra es Z")
if (a%23==15):
  print("Tu letra es S")
if (a%23==16):
  print("Tu letra es Q")
if (a%23==17):
  print("Tu letra es V")
if (a%23==18):
  print("Tu letra es H")
if (a%23==19):
  print("Tu letra es L")
if (a%23==20):
  print("Tu letra es C")
if (a%23==21):
  print("Tu letra es K")
if (a%23==22):
  print("Tu letra es E")
