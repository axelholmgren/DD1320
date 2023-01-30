from array import array

class ArrayQ:
    def __init__(self): #Skapar en tom array som kommer innehålla integers
        self.__arr = array('b')

    def enqueue(self,value): #Metod som lägger till ett värde sista i kön och tar inte en interger som indata
        self.__arr.append(value)
    
    def dequeue(self):
        return self.__arr.pop(0) #Tar bort elementet först i kön genom att popa index 0 och retunerar värdet
