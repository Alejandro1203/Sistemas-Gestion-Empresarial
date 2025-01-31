cero = ("###", "# #", "# #", "# #", "###")
uno = ("  #", "  #", "  #", "  #", "  #")
dos = ("###", "  #", "###", "#  ", "###")
tres = ("###", "  #", "###", "  #", "###")
cuatro = ("# #", "# #", "###", "  #", "  #")
cinco = ("###", "#  ", "###", "  #", "###")
seis = ("###", "#  ", "###", "# #", "###")
siete = ("###", "  #", "  #", "  #", "  #")
ocho = ("###", "# #", "###", "# #", "###")
nueve = ("###", "# #", "###", "  #", "###")

digitos = [cero, uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve]

def mostrar_numero(numero):
    for digito in str(numero):
        for i in range(5):
            print(digitos[int(digito)][i])

while True:
    numero = input("Ingresa un número entero no negativo: ")

    if not numero.isdigit():
        print("Error: Por favor ingresa un número entero no negativo.")
    else: 
        mostrar_numero(numero)