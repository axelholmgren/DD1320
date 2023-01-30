from array import array


class ArrayQ:
    def __init__(self):  # konstruktormetod som skapar en array
        self.__arr = array("b")

    def enqueue(self, value):  # Lägger in ett element på sista platsen i arrayen
        self.__arr.append(value)

    def dequeue(self):  # Tar ut och returnerar det första elementet i arrayen
        return self.__arr.pop(0)


q = ArrayQ()
q.enqueue(1)
q.enqueue(2)
x = q.dequeue()
y = q.dequeue()
if x == 1 and y == 2:
    print("OK")
else:
    print("FAILED")
