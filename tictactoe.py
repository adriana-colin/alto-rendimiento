import math
import turtle 
t = turtle.Turtle()

class TicTacToeTablero():

    def __init__(self, tamaño = 200):
        self.tamaño = tamaño
        self.t = turtle.Turtle()

    def dibuja_tablero(self):
        #Líneas verticales
        for i in range(2):
            self.t.penup()
            self.t.goto(-self.tamaño // 6 + i * self.tamaño // 3, self.tamaño // 2)
            self.t.pendown()
            self.t.goto(-self.tamaño // 6 + i * self.tamaño // 3, -self.tamaño // 2)
        
        #Líneas horizontales
        for i in range(2):
            self.t.penup()
            self.t.goto(-self.tamaño // 2, self.tamaño // 6 - i * self.tamaño // 3)
            self.t.pendown()
            self.t.goto(self.tamaño // 2, self.tamaño // 6 - i * self.tamaño //3)

    def dibuja_circulo(self, row, col):
        self.t.penup()
        center_x = -self.tamaño // 2 + col * self.tamaño // 3 + self.tamaño // 6
        center_y = self.tamaño // 2 - row * self.tamaño // 3 - self.tamaño // 6
        self.t.goto(center_x, center_y - self.tamaño // 12)
        self.t.pendown()
        self.t.circle(self.tamaño // 12)

    def dibuja_x(self, row, col):
        self.t.penup()
        start_x = -self.tamaño // 2 + col * self.tamaño // 3 + self.tamaño // 12
        start_y = self.tamaño // 2 - row * self.tamaño // 3 - self.tamaño // 12
        self.t.goto(start_x, start_y)
        self.t.pendown()
        self.t.goto(start_x + self.tamaño // 6, start_y - self.tamaño // 6)
        self.t.penup()
        self.t.goto(start_x, start_y - self.tamaño // 6)
        self.t.pendown()
        self.t.goto(start_x + self.tamaño // 6, start_y)

    def display(self):
        screen = turtle.Screen()
        self.dibuja_tablero()
        screen.mainloop()


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
 

#Prueba de las clases
if __name__ == "__main__":
    tablero = TicTacToeTablero(tamaño = 300)
    tablero.dibuja_tablero()
    tablero.dibuja_circulo(0, 0)  
    tablero.dibuja_x(0, 1)        

rect = Rectangulo(10,5)
print(rect)

circ = Circulo(7)
print(circ)

tri = Triangulo(6, 3)
print(tri)