class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root,newvalue)

    def __contains__(self,value):
        # True om value finns i trädet, False annars
        return finns(self.root,value)

    def write(self):
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def putta(nod, newvalue):
    if nod == None:
        return Node(newvalue)
    if newvalue == nod.value:   
        return nod
    if newvalue < nod.value:
        nod.left = putta(nod.left,newvalue)
        return nod
    if newvalue > nod.value:
        nod.right = putta(nod.right,newvalue)
        return nod

def finns(nod,value):
    if nod == None: 
        return False
    if value == nod.value: 
        return True
    if value < nod.value: 
        return finns(nod.left,value)
    if value > nod.value: 
        return finns(nod.right,value)


def skriv(nod):
    if nod != None:
        skriv(nod.left)
        print(nod.value)
        skriv(nod.right)