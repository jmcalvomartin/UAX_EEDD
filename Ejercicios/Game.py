import Turtle3D as tl

pantalla = tl.Screen()       # 2.  Crear pantalla
pantalla.bgcolor('lightblue')

dibujar = tl.Screen()

Leonardo = tl.Turtle()    # 3.  Crear 2 tortugas
Raphael = tl.Turtle()
Raphael.color('red')
Leonardo.color('blue')
Raphael.shape('turtle')
Leonardo.shape('turtle')

Leonardo.up()                  # 4.  Mover las tortugas a su punto de inicio
Raphael.up()
Leonardo.goto(-100,20)
Raphael.goto(-100,-20)

# Tu código empieza aquí