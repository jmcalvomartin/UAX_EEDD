#Torres de Hanoi

#Llamemos a las Torres
#A (origen)
#B (destino)
#Aux (auxiliar)

#Llamemos a los discos
#De 1 a n, siendo n el disco más grande

def hanoi(disco,TorreOrigen,TorreDestino,TorreAuxiliar):
    if disco==1:
        print("Pasar el disco de ",TorreOrigen," a ", TorreDestino)

    else:
        hanoi(disco-1,TorreOrigen,TorreAuxiliar,TorreDestino)
        print("Pasar el disco de ",TorreOrigen, " a ", TorreDestino)
        hanoi(disco-1,TorreAuxiliar,TorreDestino,TorreOrigen)

hanoi(5,"A","C","B")