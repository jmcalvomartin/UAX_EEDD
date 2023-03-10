import Turtle3D as tl
import random

class Jugador: #Creo la clase jugador
    def __init__(self,fuerza): #construyo con la fuerza que tiene ese jugador
        self.fuerza=fuerza

    def estoy(self): #Posición del jugador, lo muestra por consola
        print(tl.pos())
        print(tl.xcor())

    def andar1(self): #Desplazamiento del jugador 1
        puntero1.forward(10)

    def andar2(self): #Desplazamiento del jagador 2
        puntero2.forward(10)

class Objeto: #Creación de objetos del escenario
    def __init__(self,resistencia,color): #Construyo con resistencia y color
        self.resistencia=resistencia
        self.color=color

    def crear(self):
        self.x = random.randint(-250,250) #Lo situo de forma aleatoria en el tablero
        self.y = random.randint(-250,250)
        tl.penup()
        tl.setpos(self.x,self.y)
        tl.pendown()
        tl.color(self.color, self.color)
        tl.begin_fill() #Pinto el cuadrado que representa el objeto
        for _ in range (0,4):
            tl.forward(40)
            tl.right(90)
        tl.end_fill()

#Creo los objetos: 2 jugadores y dos tipos de objetos
tortuga=Jugador(10)
lobo=Jugador(10)
Lago=Objeto(100,"blue")
Lava=Objeto(150,"yellow")

#Configuro pantalla de juego y dos punteros para jugar a dobles
pantalla = tl.Screen()
puntero1 = tl.Turtle()
puntero2= tl.Turtle()

tl.title("Dibujo")
pantalla.setup(600, 600)
pantalla.bgcolor("orange")

#Creo la interacción con la pantalla en tiempo real
pantalla.onkey(tortuga.andar1, "q")
pantalla.onkey(tortuga.estoy, "v")
pantalla.onkey(lobo.andar2, "a")
pantalla.onkey(Lago.crear,"c")
pantalla.onkey(Lava.crear,"l")
pantalla.listen()
tl.done()