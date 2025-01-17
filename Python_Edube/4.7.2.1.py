# Import de la biblioteca random
import random

# Inicializo el tablero con números
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

# Inicializo dos constantes para pintar el teclado
ENCABEZADO_TABLERO = "+-------+-------+-------+"
RELLENO_TABLERO = "|       |       |       |"

# La función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola.
def DisplayBoard(board):
    tablero = ""

    # Bucle de 13 iteraciones para rellenar el tablero
    for index in range(13):
        if(index == 0 or index == 4 or index == 8 or index == 12):
            tablero += ENCABEZADO_TABLERO + "\n"
        elif(index == 2 or index == 6 or index == 10):
            if(index == 2):
                tablero += "|   " + str(board[0][0]) + "   |   " + str(board[0][1]) + "   |   " + str(board[0][2]) + "   |\n"
            elif(index == 6):
                tablero += "|   " + str(board[1][0]) + "   |   " + str(board[1][1]) + "   |   " + str(board[1][2]) + "   |\n"
            else:
                tablero += "|   " + str(board[2][0]) + "   |   " + str(board[2][1]) + "   |   " + str(board[2][2]) + "   |\n"
        else:
            tablero += RELLENO_TABLERO + "\n"

    print(tablero)

# La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
def EnterMove(board):
    element = int(input("Indique una posición [0, 9]: "))

    
    for sublist in board: # Bucle for que saca las sublistas del tablero        
        if(element in sublist): # Condición que busca si la posición está en alguna sublista

            # La función divmod() --> (n, n) devuelve el cociente(row) y el resto(column) 
            # para conseguir la posición exacta del elemento en el tablero
            row, column = divmod(element - 1, 3)
            board[row][column]= 'O'

# La función examina el tablero y construye una lista de todos los cuadros vacíos.
# La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
def MakeListOfFreeFields(board):
    empty_list = []


    for row in range(len(board)): # Bucle que recorre el tablero y rellena empty_list con los valores vacíos
        for column in range(len(board[0])):
            if isinstance(board[row][column], (int, float)): # isinstance() --> (boolean) indica si un elemento es de un tipo (en este caso, int o float)
                empty_list.append((row, column))

    return empty_list

# La función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
def VictoryFor(board, sign):

    
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign: # Comprobación de la diagonal primaria
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign: # Comprobación de la diagonal secundaria
        return True
    
    for index in range(3): # Comprobación de las filas y columnas 

        # all() --> (boolean) indica si todos los elementos son True o False
        if all([board[index][index2] == sign for index2 in range(3)]) or all([board[index2][index] == sign for index2 in range(3)]):
            return True

# La función dibuja el movimiento de la máquina y actualiza el tablero.
def DrawMove(board):
    list = MakeListOfFreeFields(board)

    if((1, 1) in list): # Comprobando si es el principio de la partida para colocar en medio
        board[1][1] = 'X'
    else: # Si no coloca en aleatorio
        aleatorio = int(random.uniform(0, len(list)))
        board[list[aleatorio][0]][list[aleatorio][1]] = 'X'

# La función inicia el juego
def flipflapflop():

    
    DisplayBoard(board) # Muestra tablero
    
    while not VictoryFor(board, 'O'): # Bucle hasta que alguien gane o empate
        DrawMove(board) # Mueve la máquina
        DisplayBoard(board) # Muestra tablero


        if(VictoryFor(board, 'X')): # Comprobación si gana la máquina
            print("La máquina gana")
            break

        if not MakeListOfFreeFields(board): # Comprobación si empatan
            print("El juego ha terminado en empate.")
            break

        EnterMove(board) # Mueve usuario
        DisplayBoard(board) # Muestra tablero

        if not MakeListOfFreeFields(board): # Comprobación si gana el usuario
            print("El juego ha terminado en empate.")
            break

flipflapflop()