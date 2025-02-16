class ExampleClass:
    counter = 0

    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1._ExampleClass__first, example_object_1.counter)
print(example_object_2._ExampleClass__first, example_object_2.counter)
print(example_object_3._ExampleClass__first, example_object_3.counter)

example_object_4 = ExampleClass(7)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)
print(example_object_4.__dict__, example_object_4.counter)