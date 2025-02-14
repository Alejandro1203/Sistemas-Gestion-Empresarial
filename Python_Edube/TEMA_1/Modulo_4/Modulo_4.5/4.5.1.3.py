def is_a_triangle(a, b, c):
    if(a + b <= c or a + c <= b or b + c <= a):
        return False
    return True

print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))
