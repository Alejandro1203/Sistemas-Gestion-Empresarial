row = []

for index in range(8):
    row.append("*")

print(row)

row2 = ["*" for i in range(8)]

print(row2)

squares = [x ** 2 for x in range(10)]

print(squares)

twos = [2 ** i for i in range(8)]

print(twos)

odds = [x for x in squares if x % 2 != 0]

print(odds)