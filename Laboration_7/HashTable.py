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

        hash_key = self.hashfunction(key)  # Hashar keyn
        if self.table[hash_key] is None:  # Kollar om det är tomt på indexet för den hashade nyckeln
            self.table[hash_key] = Node(key, data)  # Lägger till en nod isåntfall
        elif (
            self.table[hash_key].key == key
        ):  # Kollar om det finns en nod redan sparade med samma key
            self.table[hash_key].data = data  # Uppdaterar datan för nyckeln
        else:
            self.crash += 1  # Räknar antal krockar
            node = self.table[hash_key]  # Spar variabel för att hålla olika noder
            while (
                node.next is not None
            ):  # Loopar tills vi hittar en nod i den länkade listan som är tom
                node = node.next  # Uppdaterar node till nästa nod
                if (
                    node.key == key
                ):  # If-sats som kollar om nyckeln redan är sparad i den länkade listan
                    node.data = data  # uppdaterar datan för noden
                    return
            node.next = Node(
                key, data
            )  # Spara en ny nod när vi hittar till slutet av den länkade listan

    def search(self, key):
        """
        Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        """
        hash_key = self.hashfunction(key)
        if self.table[hash_key] is not None:
            # If-sats som kollar om det finns något sparat på hashade nyckelns index
            node = self.table[hash_key]
            while (
                node.key != key
            ):  # Letar igenom alla noder i den länkade listan tills den sökta nyckeln hittas
                node = node.next
                if (
                    node is None
                ):  # Raise KeyError om vi kommer till slutet av listan utan att ha hittat sökta nyckeln
                    raise KeyError
            return node.data  # Retunerar datan när noden med nyckeln hittas
        else:
            raise KeyError  # raise KeyError om det inte finns något sparat på indexet

    def hashfunction(self, key):
        """
        key: nyckeln
        Beräknar hashfunktionen för key
        """
        hashvalue = 0
        for char in key:
            hashvalue += len(key) * ord(char) ** 2
        return hashvalue % len(
            self.table
        )  # Mod men längden av listan för att alla index ska finnas i listan
