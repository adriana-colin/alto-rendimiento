import turtle 

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

    def dibuja_centros(self):
        centros = {}
        
        #Puntos de los centros 1,4,7
        for i in range(3):
            self.t.penup()
            self.t.goto(-self.tamaño // 3, self.tamaño // 3 - i * self.tamaño // 3)
            self.t.pendown()
            self.t.dot(10)
            centros[3 * i + 1] = self.t.position()

        #Puntos de los centros 2,5,8
        for i in range(3):
            self.t.penup()
            self.t.goto(0, self.tamaño // 3 - i * self.tamaño // 3)
            self.t.pendown()
            self.t.dot(10)
            centros[3 * i + 2] = self.t.position()

        #Puntos de los centros 3,6,9
        for i in range(3):
            self.t.penup()
            self.t.goto(self.tamaño // 3 , self.tamaño // 3 - i * self.tamaño // 3)
            self.t.pendown()
            self.t.dot(10)
            centros[3 * i + 3] = self.t.position()

            
        return centros


    def display(self):
        screen = turtle.Screen()
        self.dibuja_tablero()
        centros = self.dibuja_centros()
        print(centros)
        screen.mainloop()

if __name__ == "__main__":
    tablero = TicTacToeTablero(tamaño=300)
    tablero.display()