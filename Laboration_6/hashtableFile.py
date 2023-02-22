class Hashdict:  # Class som hanterar en dict till hashtable
    def __init__(self):
        self.table = {}  # Definerar en tom dict

    def add(self, låttitel):  # Class metod för att lägga till värden in hashtablen
        self.table[hash(låttitel)] = låttitel
