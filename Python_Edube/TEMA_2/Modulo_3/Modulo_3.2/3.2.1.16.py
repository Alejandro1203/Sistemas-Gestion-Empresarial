class Queue:
    def __init__(self):
        self.__list = []

    def put(self, elem):
        self.__list.append(elem)

    def get(self):
        val = self.__list[0]
        del self.__list[0]

        return val
    
    def length(self):
        return len(self.__list)

class SuperQueue(Queue):
    def __init__(self):
        super().__init__()

    def isempty(self):
        return super().length == 0


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(3):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")