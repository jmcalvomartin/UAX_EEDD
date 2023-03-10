#POO en Python

class Personaje:
    def __init__(self,fuerza,salud):
        #self.nombre=input("Dime el nombre: ")
        self.fuerza=fuerza
        self.salud=salud
        self.__activo=True
        self.arma=False

    #Método
    def detalle(self):
        print("Fuerza: ",self.fuerza)
        print("Salud: ",self.salud)
        print("Activo: ",self.__activo)
        print("Arma: ", self.arma)

    def deshabilitar(self):
        self.__activo=False

    def armar(self,herramienta):
        self.arma=herramienta

    def check(self):
        if self.__activo is True:
            return print("El personaje está activo")
        else:
            return print("Personaje deshabilitado")


#Herencia
class Ejercito(Personaje):
    def __init__(self,fuerza,salud,numero):
        Personaje.__init__(self,fuerza,salud)
        #super().__init__(fuerza, salud)
        self.fuerza=fuerza*numero
        self.numero=numero

    def check(self):
        super().detalle()
        print("Componentes: ", self.numero)



Soldado=Personaje(100,100)
Caballeria=Ejercito(100,100,50)
Soldado.check()
Caballeria.check()
