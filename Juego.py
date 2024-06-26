import turtle

class Tablero:
    def __init__(self):
        self.ventana = turtle.Screen()
        self.ventana.title("Juego de Gato")
        self.ventana.setup(width = 600, height = 600)
        self.ventana.bgcolor("white")
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        self.dibujar_lineas()
        self.tablero = [" " for _ in range(9)]  
        self.turno = "X"
        
    def dibujar_lineas(self):
        self.t.pensize(2)
        self.t.penup()
        self.t.goto(-300, 100)
        self.t.pendown()
        self.t.forward(600)
        self.t.penup()
        self.t.goto(-300, -100)
        self.t.pendown()
        self.t.forward(600)
        self.t.penup()
        self.t.goto(-100, 300)
        self.t.setheading(270)
        self.t.pendown()
        self.t.forward(600)
        self.t.penup()
        self.t.goto(100, 300)
        self.t.pendown()
        self.t.forward(600)
        self.t.penup()
        
    def dibujar_x(self, x, y):
        self.t.pensize(4)
        self.t.color("#EC407A")
        self.t.penup()
        self.t.goto(x - 50, y + 50)
        self.t.pendown()
        self.t.setheading(-45)
        self.t.forward(141)
        self.t.penup()
        self.t.goto(x + 50, y + 50)
        self.t.setheading(-135)
        self.t.pendown()
        self.t.forward(141)
        
    def dibujar_o(self, x, y):
        self.t.pensize(4)
        self.t.color("#26C6DA")
        self.t.penup()
        self.t.goto(x, y - 50)
        self.t.setheading(0)
        self.t.pendown()
        self.t.circle(50)
        
    def registrar_movimiento(self, posicion, jugador):
        self.tablero[posicion] = jugador
        self.actualizar_archivo()
        
    def actualizar_archivo(self):
        with open("estado_tablero.txt", "a") as archivo:
            archivo.write(f'{str(self.tablero)}\n')
            
    def registrar_resultado(self, resultado):
        with open("resultados_juegos.txt", "a") as archivo:
            archivo.write(f"Resultado del juego: {resultado}\n")
            
    def verificar_ganador(self):
        combinaciones = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]              
        ]
        for combo in combinaciones:
            if self.tablero[combo[0]] == self.tablero[combo[1]] == self.tablero[combo[2]] != " ":
                return self.tablero[combo[0]], combo
        if " " not in self.tablero:
            return "Empate", None
        return None, None
    
    def dibujar_linea_ganadora(self, combo):
        coordenadas = {
            0: (-200, 200), 1: (0, 200), 2: (200, 200),
            3: (-200, 0), 4: (0, 0), 5: (200, 0),
            6: (-200, -200), 7: (0, -200), 8: (200, -200)
        }
        x1, y1 = coordenadas[combo[0]]
        x2, y2 = coordenadas[combo[2]]
        
        self.t.pensize(4)
        self.t.speed(4)
        self.t.color("#797D7F")
        self.t.penup()
        self.t.goto(x1, y1)
        self.t.pendown()
        self.t.goto(x2, y2)
        
    def hacer_movimiento(self, x, y):
        if -300 < x < -100 and 100 < y < 300:
            posicion = 0
            coord_x, coord_y = -200, 200
        elif -100 < x < 100 and 100 < y < 300:
            posicion = 1
            coord_x, coord_y = 0, 200
        elif 100 < x < 300 and 100 < y < 300:
            posicion = 2
            coord_x, coord_y = 200, 200
        elif -300 < x < -100 and -100 < y < 100:
            posicion = 3
            coord_x, coord_y = -200, 0
        elif -100 < x < 100 and -100 < y < 100:
            posicion = 4
            coord_x, coord_y = 0, 0
        elif 100 < x < 300 and -100 < y < 100:
            posicion = 5
            coord_x, coord_y = 200, 0
        elif -300 < x < -100 and -300 < y < -100:
            posicion = 6
            coord_x, coord_y = -200, -200
        elif -100 < x < 100 and -300 < y < -100:
            posicion = 7
            coord_x, coord_y = 0, -200
        elif 100 < x < 300 and -300 < y < -100:
            posicion = 8
            coord_x, coord_y = 200, -200
        else:
            return
        
        if self.tablero[posicion] == " ":
            if self.turno == "X":
                self.dibujar_x(coord_x, coord_y)
                self.registrar_movimiento(posicion, "X")
                self.turno = "O"
            else:
                self.dibujar_o(coord_x, coord_y)
                self.registrar_movimiento(posicion, "O")
                self.turno = "X"
            
            ganador, combo_ganador = self.verificar_ganador()
            if ganador:
                self.registrar_resultado(ganador)
                if combo_ganador:
                    self.dibujar_linea_ganadora(combo_ganador)
                print(f"El ganador es {ganador}")
                self.ventana.bye()
        
    def jugar(self):
        self.ventana.onscreenclick(self.hacer_movimiento)
        self.ventana.mainloop()

class Jugador:
    def __init__(self, simbolo):
        self.simbolo = simbolo
        
tablero = Tablero()
tablero.jugar()