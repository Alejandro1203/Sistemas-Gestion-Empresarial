def factorial_function(num):
    if(num == 0):
        return None
    else:
        factorial = 1
        for index in range(2, num + 1):
            factorial *= index
        return factorial
    
print(factorial_function(1))
print(factorial_function(5))
print(factorial_function(7))

for n in range(1, 6):  # probando
    print(n, factorial_function(n))