board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
ENCABEZADO_TABLERO = "+-------+-------+-------+"
RELLENO_TABLERO = "|       |       |       |"

# La función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola.
def DisplayBoard(board):
    tablero = ""

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
# def EnterMove(board):


# def MakeListOfFreeFields(board):
#     # La función examina el tablero y construye una lista de todos los cuadros vacíos.
#     # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.

# def VictoryFor(board, sign):
#     # La función analiza el estatus del tablero para verificar si
#     # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.

# def DrawMove(board):
#     # La función dibuja el movimiento de la máquina y actualiza el tablero.

DisplayBoard(board)
print(board[0][0])