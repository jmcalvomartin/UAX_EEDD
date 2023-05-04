#Listas

invitados=["Raúl","Ana","Cristina","Javi",34,76]
#print(invitados[-1][2])
#print(len(invitados))


for x in range(len(invitados)):
    if isinstance(invitados[x],list):
        for y in range(len(invitados[x])):
            print(invitados[x][y])
    else:
        print(invitados[x])


for invitado in invitados:
    if isinstance(invitado,list):
        for x in invitado:
            print(x)
    else:
        print(invitado)

