import math

class FiguraGeometrica():

    def __init__(self):
        self.ubicacion_x = 0
        self.ubicacion_y = 0

    def dibujaFigura(self):
        None

    def modificar_x(self, x):
        self.ubicacion_x = x
    
    def modificar_y(self, y):
        self.ubicacion_y = y
    
class Rectangulo(FiguraGeometrica):
    
    def __init__(self,alto,base):
        self.alto = float(alto)
        self.base = float(base)

    def __str__(self):
        return "Es un rectangulo, con area: " + str(self.get_area())
        
    def get_area(self):
        return self.alto * self.base


class Circulo(FiguraGeometrica):

    def __init__(self, radio):
        self.radio = float(radio)
    
    def __str__(self):
        return "Es un círculo, con área: " + str(self.get_area())
    
    def get_area(self):
        return math.pi * (self.radio ** 2)
class Triangulo(FiguraGeometrica):

    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)

    def __str__(self):
        return "Este es un trángulo, con área: " + str(self.get_area())
    
    def get_area(self):
        return (self.base * self.altura) / 2
 
# Aqui empiza nuestro codigo
#import turtle
import turtle 
t = turtle.Turtle()

class TicTacToeTablero():

    def __init__(self, tamaño = 200):
        self.tamaño = tamaño

    def dibuja_tablero(self):
        t.penup()
        t.goto(-self.tamaño // 2, self.tamaño //6)
        t.pendown()
        t.forward(self.tamaño)

        t.penup()
        t.goto(-self.tamaño // 2, -self.tamaño //6)

        t.penup()
        t.forward(self.tamaño)

        t.penup()
        t.goto(-self.tamaño // 6, self.tamaño //2)
        t.pendown()
        t.forward(self.tamaño)

    def display(self):
        screen = turtle.Screen()
        self.dibuja_tablero()
        screen.mainloop()

#t = ture.turtle
#prueba = Rectangulo(2,2)
#prueba.dibujaFigura(t)

#Prueba de las clases
tablero = TicTacToeTablero(300)
tablero.display()

rect = Rectangulo(10,5)
print(rect)

circ = Circulo(7)
print(circ)

tri = Triangulo(6, 3)
print(tri)