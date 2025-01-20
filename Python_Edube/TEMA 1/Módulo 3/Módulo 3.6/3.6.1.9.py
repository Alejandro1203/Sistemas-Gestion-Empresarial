my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
sinDuplicados = []

for index in my_list:
    if index not in sinDuplicados:
        sinDuplicados.append(index)


print("La lista con elementos únicos:", sinDuplicados)
# print("La lista con elementos únicos:", set(my_list))
print(my_list)