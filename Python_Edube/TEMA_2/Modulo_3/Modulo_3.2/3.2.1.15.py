class Queue:
    def __init__(self):
        self.__list = []

    def put(self, elem):
        self.__list.append(elem)

    def get(self):
        val = self.__list[0]
        del self.__list[0]

        return val


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(5):
        print(que.get())
except:
    print("Error de Cola")