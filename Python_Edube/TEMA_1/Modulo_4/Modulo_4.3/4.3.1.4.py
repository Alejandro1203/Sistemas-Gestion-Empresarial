def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

list = [2 , 3, 45, 6]
print(list_sum(list))

print(list_sum(3))