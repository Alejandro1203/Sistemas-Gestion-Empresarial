import math, random

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
def EnterMove(board):
    posicion = int(input("Indique una posición: "))

    for sublist in board:
        if(posicion in sublist):
            row, col = divmod(posicion - 1, 3)
            board[row][col]= 'O'



#     # La función examina el tablero y construye una lista de todos los cuadros vacíos.
#     # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
def MakeListOfFreeFields(board):
    empty_list = []

    for row in range(len(board)):
        for column in range(len(board[0])):
            if isinstance(board[row][column], (int, float)):
                empty_list.append((row, column))
            # if(not math.isnan(board[row][column])):
            #     empty_list.append((row, column))

    return empty_list

# La función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
def VictoryFor(board, sign):

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    
    for index in range(3):
        if all([board[index][index2] == sign for index2 in range(3)]) or all([board[index2][index] == sign for index2 in range(3)]):
            return True



# La función dibuja el movimiento de la máquina y actualiza el tablero.
def DrawMove(board):
    list = MakeListOfFreeFields(board)

    if((1, 1) in list):
        board[1][1] = 'X'
    else:
        aleatorio = int(random.uniform(0, len(list)))
        board[list[aleatorio][0]][list[aleatorio][1]] = 'X'

# La función inicia el juego
def flipflapflop():

    DisplayBoard(board)
    
    while not VictoryFor(board, 'O'):
        DrawMove(board)
        DisplayBoard(board)

        if(VictoryFor(board, 'X')):
            print("La máquina gana")
            break

        if not MakeListOfFreeFields(board):
            print("El juego ha terminado en empate.")
            break

        EnterMove(board)
        DisplayBoard(board)

        if not MakeListOfFreeFields(board):
            print("El juego ha terminado en empate.")
            break

flipflapflop()