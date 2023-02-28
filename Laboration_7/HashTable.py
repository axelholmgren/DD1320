class Node:
    def __init__(self, key="", data=None):
        self.key = key
        self.data = data
        self.next = None


class Hashtable:
    def __init__(self, size):
        """
        size: hashtabellens storlek
        """
        self.table = [None] * (size * 2)
        self.crash = 0

    def store(self, key, data):
        """key: nyckeln
        data: objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen.
        """
        # root = self.table[self.hashfunction(key)] <---- användbar omskriving
        if self.table[self.hashfunction(key)] is None:
            self.table[self.hashfunction(key)] = Node(key, data)
        else:
            self.crash += 1
            node = self.table[self.hashfunction(key)].next
            while node is not None:
                node = node.next
            node = Node(key, data)

    def search(self, key):
        """
        key: nyckeln
        Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska vi få en Exception, KeyError
        """
        # Fyll i kod här!
        try:
            if self.table[self.hashfunction(key)] is not None:
                node = self.table[self.hashfunction(key)]
                print(node.key)
                print(key)
                while node.key != key:
                    node = node.next
                    if node is None:
                        print("fel 1")
                        raise KeyError
                return node.data
            else:
                print("fel 2")
                raise KeyError
        except KeyError:
            return "Finns ej"

    def hashfunction(self, key):
        """
        key: nyckeln
        Beräknar hashfunktionen för key
        """
        hashvalue = 0
        for i, char in enumerate(key):
            hashvalue += (i + 3) ** (3 + ord(char)) + i
        return hashvalue % len(self.table)
