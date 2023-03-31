from molgrafik import *


class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None

def main():
    mol = Ruta(atom="Cl", num=2)
    mg = Molgrafik()
    mg.show(mol)
    while True:
        pass

if __name__ == '__main__':
    main()