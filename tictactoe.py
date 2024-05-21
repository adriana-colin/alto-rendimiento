import math

class FiguraGeometrica():

    def __init__(self):
        self.ubicacion_x = 0
        self.ubicacion_y = 0

    def dibujaFigura(self):
        None
        
    def get_area(self):
        return 999999999.9

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
    
    base = 0.0
    altura = 0.0

    def __init__(self, base, altura):
        self.base = float(base)
        self.altura = float(altura)

    def __str__(self):
        return "Este es un trángulo, con área: " + str(self.get_area())
    
    def get_area(self):
        return (self.base * self.altura) / 2



    
# Aqui empiza nuestro codigo
#import turtle

#t = turtle.turtle
#prueba = Rectangulo(2,2)
#prueba.dibujaFigura(t)

#Prueba de las clases
rect = Rectangulo(10,5)
print(rect)

circ = Circulo(7)
print(circ)

tri = Triangulo(6, 3)
print(tri)