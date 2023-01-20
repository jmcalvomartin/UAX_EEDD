#Ataque de fuerza bruta sobre un código PIN de 4 números

# En este ejercicio realizamos la busqueda del número PIN usando la aleatoriedad del comando randint, generando números aleatorios entre 0 y 9999.

import random  # Libreria de Python para crear números aleatorios
import time  # Libreria para controlar el tiempo de los procesos

#password = str(input("Introduce tu PIN de 4 digitos: "))  # Pedimos un PIN al usuario para hacer una prueba

hack = ""  # variable que usaremos para guardar las combinaciones que generamos
hack_l = random.sample(range(0, 9999), 9999) #Creamos la lista de números únicos

for password in ["2347","6512","7800","0101","0045","4545"]:
        inicio = time.time()  # Capturo el tiempo de inicio del proceso de busqueda

        while hack != password:  # Mientras mis combinaciones sean diferentes al password original continuo
            hack = str(random.randint(0, 9999))  # Genero números aleatorios entre 0 y 9999
            # print(hack) #Descomentalo para ver las combinaciones que va generando, pero el programa va más lento

            if len(hack)<4: #Controlo que tenga menos de 4 caracteres
                hack="0"*(4-len(hack)) + hack

            if (hack == password):  # Si lo encuentra lo imprime
                print("Tu PIN es " + hack)
                break

            else:
                continue  # Si no coincide continuo

        fin = time.time()  # Capturo el tiempo de finalización

        print("tu programa aletorio ha tardado " + str(fin - inicio) + " segundos")

        #-----------------------------------------------------------------------------------------------------------------
        # Programa con lista

        inicio = time.time()  # Capturo el tiempo de inicio del proceso de busqueda
        x=""
        while str(x) != password:  # Mientras mis combinaciones sean diferentes al password original continuo
            for x in hack_l:

                if len(str(x))<4: #Controlo que tenga menos de 4 caracteres
                    x="0"*(4-len(str(x))) + str(x)

                if (str(x) == password):  # Si lo encuentra lo imprime
                    print("Tu PIN es " + str(x))
                    break

                else:
                    continue  # Si no coincide continuo

        fin = time.time()  # Capturo el tiempo de finalización

        print("tu programa con lista ha tardado " + str(fin - inicio) + " segundos")
        print("-------------------------------------------------------------------")