from random import randint, choice, sample

for i in range(10):
    print(randint(1, 10), end=',')

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print()
print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

from platform import version

print(version())
