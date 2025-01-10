my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
sinDuplicados = []

for i in my_list:
    if i not in sinDuplicados:
        sinDuplicados.append(i)


print("La lista con elementos únicos:" + str(sinDuplicados))
print("La lista con elementos únicos:" + str(set(my_list)))
print(my_list)