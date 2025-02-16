def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]

    return val



stack = []

push(2)
push(2)
push(2)
push(2)

print(stack)

pop()

print(stack)