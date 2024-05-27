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

    def display(self):
        screen = turtle.Screen()
        self.dibuja_tablero()
        screen.mainloop()

class FiguraGeometrica:
    def __init__(self):
        self.ubicacion_x = 0
        self.ubicacion_y = 0
        self.t = turtle.Turtle()

    def dibuja_figura(self):
        pass

    def modificar_x(self, x):
        self.ubicacion_x = x

    def modificar_y(self, y):
        self.ubicacion_y = y

class Circulo(FiguraGeometrica):

    def __init__(self, radio):
        self.radio = float(radio)
        self.t = turtle.Turtle()


    def dibuja_circulo(self, row, col, tamaño):
        self.t.penup()
        center_x = -tamaño // 3 + col * tamaño // 3 + tamaño //6
        center_y = tamaño // 3 - row * tamaño // 3 - tamaño // 6
        self.t.goto(center_x, center_y - tamaño // 12)
        self.t.pendown()
        self.t.circle(tamaño // 12)

class Tachita(FiguraGeometrica):
    
    def __init__(self, tamaño = 200):
        self.t = turtle.Turtle()

    def dibuja_x(self, row, col, tamaño):
        self.t.penup()
        start_x = -tamaño // 3 + col * tamaño // 3 + tamaño // 12
        start_y = tamaño // 3 - row * tamaño // 3 - tamaño // 12
        self.t.goto(start_x, start_y)
        self.t.pendown()
        self.t.goto(start_x + self.tamaño // 6, start_y - self.tamaño // 6)
        self.t.penup()
        self.t.goto(start_x, start_y - self.tamaño // 6)
        self.t.pendown()
        self.t.goto(start_x + self.tamaño // 6, start_y)

def obtener_coordenadas():
    while True:
        try:
            row = int(input("Introduce la fila (0, 1, 2): "))
            col = int(input("Introduce la columna (0, 1, 2): "))
            if row in [0, 1, 2] and col in [0, 1, 2]:
                return row, col
            else:
                print("Por favor, introduce valores válidos para fila y columna (0, 1, 2).")
        except ValueError:
            print("Por favor, introduce números válidos.")
 

#Prueba de las clases
if __name__ == "__main__":
    tablero = TicTacToeTablero(tamaño=300)
    tablero.dibuja_tablero()

    while True:
        figura = input("¿Qué figura quieres dibujar? (circulo/x/salir): ").lower()
        if figura == "salir":
            break

        row, col = obtener_coordenadas()

        if figura == "circulo":
            circulo = Circulo(radio=50)
            circulo.dibuja_circulo(row, col, tamaño=300)
        elif figura == "x":
            tachita = Tachita(altura=100, ancho=100)
            tachita.dibuja_x(row, col, tamaño=300)
        else:
            print("Figura no reconocida. Por favor, elige 'circulo' o 'x'.")

    turtle.done()