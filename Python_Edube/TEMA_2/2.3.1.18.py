def mysplit(strng):
    if not isinstance(strng, str):
        return None
    else:
        lista = []
        cadena = ""

        for index in range(len(strng)):
            if strng[index] != " ":
                cadena += strng[index]
            elif cadena != "":
                lista.append(cadena)
                cadena = ""  

        return lista 

print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))