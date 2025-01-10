libros = {
 "Cien años de soledad": ["Realismo mágico", "Drama"],
 "El señor de los anillos": ["Fantasía", "Aventura"],
 "1984": ["Distopía", "Política", "Drama"],
 "Don Quijote": ["Clásico", "Aventura"]
}

libros_invertido = {}

for values in libros.values():
    for value in values:
        if value not in libros_invertido.keys():
            libros_invertido[value] = []

for key in libros.keys():
    for values in libros[key]:
        libros_invertido[values].append(key)
        

print(libros_invertido)
