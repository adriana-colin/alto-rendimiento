import turtle 

class TicTacToeTablero():
    
    def __init__(self, tamaño = 200):
        self.tamaño = tamaño
        self.t = turtle.Turtle()
        self.t.speed(20)
        self.centros = {}

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

    def obtener_centros(self):

        #Puntos de los centros 1,4,7
        for i in range(3):
            self.t.penup()
            self.t.goto(-self.tamaño // 3, self.tamaño // 3 - i * self.tamaño // 3)
            self.centros[3 * i + 1] = self.t.position()

        #Puntos de los centros 2,5,8
        for i in range(3):
            self.t.penup()
            self.t.goto(0, self.tamaño // 3 - i * self.tamaño // 3)
            self.centros[3 * i + 2] = self.t.position()

        #Puntos de los centros 3,6,9
        for i in range(3):
            self.t.penup()
            self.t.goto(self.tamaño // 3 , self.tamaño // 3 - i * self.tamaño // 3)
            self.centros[3 * i + 3] = self.t.position()

        return self.centros
    
    
    def display(self):
        screen = turtle.Screen()
        self.dibuja_tablero()
        centros = self.obtener_centros()
        print(centros)
        #screen.mainloop()

class circulo():
    
    t = turtle.Turtle()

    def __init__(self, coord_x, coord_y, radio = 20):
        self.radio = radio
        self.t = turtle.Turtle()
        self.coord_x = float(coord_x)
        self.coord_y = float(coord_y)

    def dibujar(coord_x, coord_y):
        t = turtle.Turtle()
        t.pensize(4)
        t.color("blue")
        t.penup()
        t.goto(coord_x, coord_y)
        t.left(270)
        t.forward(40)
        t.left(90)
        t.pendown()
        t.circle(40)
        t.penup()

class tachita():
    
    t = turtle.Turtle()

    def __init__(self, coord_x, coord_y, tamaño = 28):
        #self.t = turtle.Turtle()
        self.tamaño = float(tamaño)
        self.coord_x = float(coord_x)
        self.coord_y = float(coord_y)

    def dibujar(coord_x, coord_y):
        t = turtle.Turtle()
        t.pensize(4)
        t.color("red")
        t.penup()
        t.goto(coord_x, coord_y)
        t.forward(35)
        t.left(90)
        t.forward(35)
        t.left(135)
        t.pendown()
        t.forward(97)
        t.penup()
        t.right(180)
        t.forward(97)
        t.left(225)
        t.forward(70)
        t.left(225)
        t.pendown()
        t.forward(97)
        t.penup

"""
class Jugador():

    def __init__(self, ficha):
        if ficha == "x":
            self.ficha = True
        else:
            self.ficha = False

class JuegoGato():

    def __init__(self, jugador1, jugador2):

        t = turtle.Turtle()

        self.jugador1 = jugador1
        self.jugador2= jugador2

        self.quiensigue = True

    def nohayganador(self):
        return True

    def jugada(self,columna, fila):
        coordenada_fila = 30 * fila
        coordenada_columna = 30 * columna

        self.quiensigue = not self.quiensigue

        if self.quiensigue:
            jugada_1 = circulo(self.t, 10,coordenada_columna,coordenada_fila)
        else:
            jugada_1 = tachita(self.t, 10,coordenada_columna,coordenada_fila)
        
        jugada_1.dibujar()
"""
            


if __name__ == "__main__":
    tablero = TicTacToeTablero(tamaño=300)
    tablero.display()

    jugadas = {
        "1": [-100,100],
        "2": [-100,0],
        "3": [-100,-100],
        "4": [0,-100],
        "5": [0,0],
        "6": [0,100],
        "7": [100,-100],
        "8": [100,0],
        "9": [100,100],
    }

    

    for i in range(9):

        jugada = input("dame la jugada")
        circulo.dibujar(jugadas[jugada][0], jugadas[jugada][1])
        jugada = input("dame la jugada")
        tachita.dibujar(jugadas[jugada][0], jugadas[jugada][1])
    
    screen = turtle.Screen()
    screen.mainloop()

#del diccionario para las posiciones jugables restantes