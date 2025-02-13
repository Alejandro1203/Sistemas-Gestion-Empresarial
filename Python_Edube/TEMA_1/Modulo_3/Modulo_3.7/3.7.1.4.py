temps = [[0.0 for h in range(24)] for j in range(31)]

total = 0.0
highest = -275 

for day in temps:
    for temps in day:
        if temps > highest:
            highest = temps

average = total / 31

print("Average temperature at noon:", average)
print("Highest:", highest)