class Node:
    # Skapar en Node med ett värde och en pekare till nästa nod.
    def __init__(self, value):
        self.value = value  # Attribut av datatyp string
        self.next = None  # Attribut av klassen Node


class LinkedQ:

    # Skapar en kö (tom)
    def __init__(self):  # Skapar kön  tom med None som första och sista element
        self.__first = None  # Objekt av klassen Node
        self.__last = None  # Objekt av klassen Node

    # Reurnerar sant/falskt beroende på om det finns något på första platsen i kön
    def isEmpty(self):
        if self.__first == None:  # True om det inte finns ett första element
            return True
        else:
            return False

    # Tar in värdet value, kollar om kön är tom.
    # Om tom lägg till en Node och sätt både första och sista pekaren till Node
    # Om inte tom ta ut pekaren som pekar längst bak i kön, skapa en Node längst bak i
    # kön sätt pekaren från den gamla sista till nya sistapekaren
    def enqueue(self, value):
        if self.isEmpty():
            self.__first = Node(value)
            self.__last = self.__first
        else:
            temp = self.__last
            self.__last = Node(value)
            temp.next = self.__last

    # Tar ut förstapekaren. Om next attributet  är None uppdatera förstapekaren till None
    # Om det finns något efter sätt de näst första pekaren till förstapekaren
    # Returnera värdet på det som låg på plats 1 i kön
    def dequeue(self):
        temp = self.__first
        if temp.next == None:
            self.__first = None
        else:
            self.__first = temp.next
        return temp.value

    # Räknar antalet element tills att det nästa elementet är None (tomt), retunerar antalet element i kön
    def size(self):
        counter = 0
        node_count = self.__first.next
        while node_count.next != None:  # Loopar tills att next pekaren pekar på None
            counter += 1
            node_count = node_count.next
        return counter
