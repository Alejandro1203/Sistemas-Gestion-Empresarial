def mysplit(strng):
    if not isinstance(strng, str):
        return "No es String"
    else:
        lista = []
        cadena = ""

        for chr in strng:

            if chr != " ":
                cadena += chr
            elif cadena != "":
                lista.append(cadena)
                cadena = ""

        if cadena != "":
            lista.append(cadena)

        return lista


print(mysplit(2))
print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))