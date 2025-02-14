try:
    value = input("Ingresa un número natural: ")
    print(2/int(value))
except ValueError:
    print("No es el tipo que es broco")
except ZeroDivisionError:
    print("No dividas entre 0")