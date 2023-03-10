import Turtle3D as tl

class Jugador:
    def __init__(self,size,color):
        self.size=size
        self.color=color
        self.fuerza=100

    def tablero(self,x,y):
        self.x=x
        self.y=y
        tl.penup()
        tl.goto(x,y)
        tl.pendown()
        tl.color(self.color,self.color)
        tl.begin_fill()
        tl.circle(self.size)
        tl.end_fill()

    def andar(self):
        tl.forward(10)

    def lugar(self):
        print("Estoy en la posición: ", tl.pos())

#Crear pantalla
pantalla=tl.Screen()
tl.title("Dibujo")
pantalla.setup(600,600)
tl.shape("turtle")


tortuga=Jugador(30,"green")
tortuga.tablero(200,200)

lobo=Jugador(40,"gray")
lobo.tablero(-200,-200)

pantalla.onkey(tortuga.andar,"q")
pantalla.onkey(tortuga.lugar,"l")
pantalla.listen()

tl.done()