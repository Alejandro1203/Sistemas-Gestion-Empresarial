# paso 1
Beatles = []
print("Paso 1:", Beatles)

# paso 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# paso 3
for index in range(2):
    Beatles.append(input("Introduzca un miembro: "))

print("Paso 3:", Beatles)

# paso 4
del(Beatles[4])
del(Beatles[3])
print("Paso 4:", Beatles)

# paso 5
Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)


# probando la longitud de la lista
print("Los Fav", len(Beatles))