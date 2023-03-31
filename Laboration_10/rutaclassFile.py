from molgrafik import *
import sys
import tkinter as tk


class Ruta:
    def __init__(self, atom="( )", num=1):
        self.atom = atom
        self.num = num
        self.next = None
        self.down = None


mol = Ruta(atom="Cl", num=2)
mg = Molgrafik()
mg.show(mol)
pause = sys.stdin.readline()
