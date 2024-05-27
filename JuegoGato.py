import turtle 

class TicTacToeTablero():
    
    def __init__(self, tamaño = 200):
        self.tamaño = tamaño
        self.t = turtle.Turtle()
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

    def dibuja_centros(self):

        #Puntos de los centros 1,4,7
        for i in range(3):
            self.t.penup()
            self.t.goto(-self.tamaño // 3, self.tamaño // 3 - i * self.tamaño // 3)
            self.t.pendown()
            self.t.dot(10)
            self.centros[3 * i + 1] = self.t.position()

        #Puntos de los centros 2,5,8
        for i in range(3):
            self.t.penup()
            self.t.goto(0, self.tamaño // 3 - i * self.tamaño // 3)
            self.t.pendown()
            self.t.dot(10)
            self.centros[3 * i + 2] = self.t.position()

        #Puntos de los centros 3,6,9
        for i in range(3):
            self.t.penup()
            self.t.goto(self.tamaño // 3 , self.tamaño // 3 - i * self.tamaño // 3)
            self.t.pendown()
            self.t.dot(10)
            self.centros[3 * i + 3] = self.t.position()

        return self.centros
    
    
    def display(self):
        screen = turtle.Screen()
        self.dibuja_tablero()
        centros = self.dibuja_centros()
        print(centros)
        #screen.mainloop()

class circulo():
    
    t = turtle.Turtle()

    def __init__(self, radio = 20):
        self.radio = radio
        self.t = turtle.Turtle()

    def dibujar():
        t = turtle.Turtle()
        t.penup()
        t.goto(0,100)
        t.left(270)
        t.forward(40)
        t.left(90)
        t.pendown()
        t.circle(40)

class tachita():
    
    t = turtle.Turtle()

    def __init__(self, tamaño = 28):
        #self.t = turtle.Turtle()
        self.tamaño = float(tamaño)

    def dibujar():
        t = turtle.Turtle()
        t.penup()
        t.goto(-100,100)
        t.left(45)
        t.forward(40)
        t.left(180)
        t.pendown()
        t.forward(80)
        t.penup()
        t.goto(-71.72,71.72)
        t.right(90)
        t.pendown()
        t.forward(80)

if __name__ == "__main__":
    tablero = TicTacToeTablero(tamaño=300)
    tablero.display()
    circulo.dibujar()
    tachita.dibujar()
    screen = turtle.Screen()
    screen.mainloop()