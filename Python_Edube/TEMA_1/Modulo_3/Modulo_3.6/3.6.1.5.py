my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

del my_list[1:3]
print(my_list)

del my_list[:]
print(my_list)

del my_list
print(my_list)