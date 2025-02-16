class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val

example_class_1 = ExampleClass()
example_class_2 = ExampleClass(2)

example_class_2.set_second(3)

example_class_3 = ExampleClass(4)
example_class_3.__third = 5

print(example_class_1.__dict__)
print(example_class_2.__dict__)
print(example_class_3.__dict__)
print(example_class_1._ExampleClass__first)
print(example_class_2._ExampleClass__second)
print(example_class_3.__third)