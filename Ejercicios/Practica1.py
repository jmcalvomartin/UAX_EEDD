'''
Saca por pantalla "Asignatura de TIC" usando variable
Saca por pantalla lo mismo que antes pero la variable solo puede contener el valor "TIC"
Saca por pantalla mi nombre es " ", pero solo puedes pedirle al usuario su nombre.
(OJO elnombre siempre debe salir en mayúscula)
'''
a="Asignatura de TIC"
print(a)

b="TIC"
print("Asignatura de ",b)

name=input("Dime tu nombre: ")
print("Mi nombre es ",name.upper())

'''
Le pido al usuario su nombre y su nacionalidad y después saco por pantalla:
Ejemplo
"Aitor" tiene la nacionalidad "Francesa"
'''
name=input("Dime tu nombre: ")
nacionalidad=input("Dime la nacionalidad: ")

print(name.upper()," mi nacionalidad es ", nacionalidad.lower())

'''
Necesito un programa que realice el teorema de Pitágoras. Debe pedirle al usuario lalongitud de los 2 catetos y devolverle el valor de la hipotenusa.
Tambien debe decirle el valor total del perimetro del triangulo.
'''
c1=int(input("Dime un lado: "))
c2=int(input("Dime otro lado: "))

h=(c1**2+c2**2)**(1/2)
print("La hipotenusa es ", h , " y el perimetro es ",(c1+c2+h))