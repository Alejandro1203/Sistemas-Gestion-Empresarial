def read_int(prompt, min, max):
    while True:
        valor = input(prompt)

        comp = valor.lstrip("-")

        if not comp.isnumeric():
                print("Error: entrada incorrecta")
                continue
        else:
            valor = int(valor)

            if valor > max or valor < min:
                 print("Error: el valor no está dentro del rango permitido (min..max)")
                 continue
            else:
                 return valor


v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)

print("El número es:", v)