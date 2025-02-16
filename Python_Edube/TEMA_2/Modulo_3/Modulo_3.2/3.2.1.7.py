class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]

        return val

stack_object = Stack()
stack_object.push(2)
stack_object.push(5)
stack_object.push(7)
stack_object.push(4)
stack_object.push(1)

print(stack_object)

stack_object.pop
stack_object.pop
stack_object.pop

print(stack_object)