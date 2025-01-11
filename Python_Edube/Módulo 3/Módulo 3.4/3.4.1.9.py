my_list = [] 
other_list = [] # Creando una lista vacía.

for index in range(5):
    my_list.append(index + 1)
    other_list.insert(0, index + 1)

print(my_list)
print(other_list)