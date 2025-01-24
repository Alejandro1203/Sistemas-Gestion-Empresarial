import random

# Esta función rellena aleatoriamente el tablero con células vivas ('*') o muertas (' ')
def tableroCelulas(tablero, tamanyo):
    tablero = [['' for _ in range(tamanyo)]for _ in range(tamanyo)]

    for index in range(tamanyo):
        for index2 in range(tamanyo):
            tablero[index][index2] = random.choice(['*', ' '])

    return tablero

def pintarTablero(tablero):
    SEPARADOR = '-----'

    print(SEPARADOR * len(tablero))

    for index in range(len(tablero)):      

        for index2 in range(len(tablero)):
            print('| ' + tablero[index][index2] + ' |', end='')
        print('\n' + (SEPARADOR * len(tablero)))
        

def juegoVida():
    tablero = []
    tamanyo = int(input("Introduce el tamaño del tablero: "))

    tablero = tableroCelulas(tablero, tamanyo)

    pintarTablero(tablero)


juegoVida()




