#Ataque de fuerza bruta sobre un código PIN de 4 números

# En este ejercicio realizamos la busqueda del número PIN usando la aleatoriedad del comando randint, generando números aleatorios entre 0 y 9999.

import random  # Libreria de Python para crear números aleatorios

password = input("Introduce tu PIN de 4 digitos: ")  # Pedimos un PIN al usuario para hacer una prueba

hack = ""  # variable que usaremos para guardar las combinaciones que generamos


while hack != password:  # Mientras mis combinaciones sean diferentes al password original continuo
    hack = str(random.randint(0, 9999))  # Genero números aleatorios entre 0 y 9999
    print(hack) #Descomentalo para ver las combinaciones que va generando, pero el programa va más lento


    if (hack == password):  # Si lo encuentra lo imprime
        print("Tu PIN es " + hack)
        break

    else:
        continue  # Si no coincide continuo
