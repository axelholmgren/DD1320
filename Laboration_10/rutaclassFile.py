class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.weight = 0
        self.next = None
        self.down = None
