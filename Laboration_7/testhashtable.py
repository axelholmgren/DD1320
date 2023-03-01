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
        self.crashlist = []

    def store(self, key, data):
        """key: nyckeln
        data: objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen.
        """

        hash_key = self.hashfunction(key)
        if self.table[hash_key] == None:
            self.table[hash_key] = Node(key, data)
            return
        if self.table[hash_key].key == key:
            self.table[hash_key].data = data
            return
        self.crash += 1
        self.crashlist.append(key)
        node = self.table[hash_key]
        while node.next is not None:
            if node.key == key:
                node.data = data
                return
            self.crash += 1
            node = node.next
        node.next = Node(key, data)

    def search(self, key):
        """
        key: nyckeln
        Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska vi få en Exception, KeyError
        """
        hash_key = self.hashfunction(key)
        if self.table[hash_key] is not None:
            node = self.table[hash_key]
            while node.key != key:
                node = node.next
                if node is None:
                    raise KeyError
            return node.data
        raise KeyError

    def hashfunction_2(self, key):
        """
        key: nyckeln
        Beräknar hashfunktionen för key
        """
        hashvalue = 0
        for i, char in enumerate(key):
            hashvalue += 21 * ord(char)
        return hashvalue % len(self.table)

    def hashfunction(self, key):
        result = 0
        for c in key:
            result = result * 32 + ord(c)
        return result % len(self.table)
