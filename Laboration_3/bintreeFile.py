# klass skapar ett binärt träd
class Bintree:
    def __init__(self):  # Ett attribut som är en root, tillhör klassen Node
        self.root = None

    def put(
        self, newvalue
    ):  # Metod som lägger in ett nytt värde i trädet, tar newvalue som indata
        self.root = putta(self.root, newvalue)

    def __contains__(
        self, value
    ):  # Metod som letar upp ett värde i trädet, tar value som indata
        return finns(self.root, value)

    def write(self):  # Metod som skriver ut trädets värden i inorder (lägst till högst)
        skriv(self.root)
        print("\n")


# klass som skapar en nod (objekt) med ett värde samt två pekare left, right
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Fuktion som tar in newvalue som indata och placerar en nod på rätt position i trädet
def putta(nod, newvalue):
    if nod is None:  # Om noden inte finns är trädet tomt och den nya noden blir root
        return Node(newvalue)
    if (
        newvalue == nod.value
    ):  # Om värdet på noden och det nya värdet är lika returnerar vi noden
        # (lämnar oförändrard)
        return nod
    if (
        newvalue < nod.value
    ):  # Om det nya värdet är mindre än det värdet i noden, kallar rekursivt och
        # uppdaterar den nya positionen
        nod.left = putta(nod.left, newvalue)
        return nod
    if (
        newvalue > nod.value
    ):  # Om det nya värdet är större än det värdet i noden, kallar rekursivt och
        # uppdaterar den nya positionen
        nod.right = putta(nod.right, newvalue)
        return nod


# Denna kod är tagen från Föreläsningsanteckningar 5, DD1320, Sten Andersson
# Funktion som tar in ett värde och letar upp om värdet finns
def finns(nod, value):
    if nod is None:  # Om noden inte finns finns inget i trädet, returnerar falskt
        return False
    if (
        value == nod.value
    ):  # Om värdet är samma som värdet på noden finns värdet, returnerar falskt
        return True
    if (
        value < nod.value
    ):  # Om värdet är mindre än värdet på noden kallas funktionen rekursivt och
        # uppdaterar positionen
        return finns(nod.left, value)
    if (
        value > nod.value
    ):  # Om värdet är större än värdet på noden kallas funktionen rekursivt och
        # uppdaterar positionen
        return finns(nod.right, value)


# Funktion som skriver ut trädet i inorder (minst till störst)
def skriv(nod):
    if nod is not None:
        skriv(nod.left)
        print(nod.value)
        skriv(nod.right)
