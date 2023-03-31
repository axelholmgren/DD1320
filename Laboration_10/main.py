import sys
from LinkedQueue import LinkedQ
from molgrafik import *
from rutaclassFile import Ruta


class SyntaxFel(Exception):
    pass


def regel_formel(kö):
    if kö.isEmpty() is True:
        raise SyntaxFel("Saknad gruppstart vid radslutet " + str(kö))
    mol = regel_molekyl(kö)
    if kö.isEmpty() is False and kö.peek() == ")":
        raise SyntaxFel("Felaktig gruppstart vid radslutet " + str(kö))
    return mol


def regel_molekyl(kö):
    mol = regel_grupp(kö)
    if kö.isEmpty() is False and kö.peek() != ")":
        mol.next = regel_molekyl(kö)
    return mol


def regel_grupp(kö):
    rutan = Ruta()
    if kö.peek() == "(":
        kö.dequeue()
        rutan.down = regel_molekyl(kö)
        if kö.peek() == ")":
            kö.dequeue()
            rutan.atom = "( )"
            if kö.peek() is None:
                raise SyntaxFel("Saknad siffra vid radslutet")
            else:
                rutan.num = regel_nummer(kö)
        else:
            raise SyntaxFel("Saknad högerparentes vid radslutet")  # kanke med str(kö)
    else:
        rutan.atom = regel_atom(kö)
        if kö.isEmpty() is False:
            if kö.peek() in "0123456789":
                rutan.num = regel_nummer(kö)
    return rutan


def regel_atom(kö):
    bok = regel_första_bok(kö)
    if kö.isEmpty() is False and kö.peek() in "abcdefghijklmnopqrstuvwxyz":
        bok += str(regel_andra_bok(kö))
    if bok.strip() not in [
        "H",
        "He",
        "Li",
        "Be",
        "B",
        "C",
        "N",
        "O",
        "F",
        "Ne",
        "Na",
        "Mg",
        "Al",
        "Si",
        "P",
        "S",
        "Cl",
        "Ar",
        "K",
        "Ca",
        "Sc",
        "Ti",
        "V",
        "Cr",
        "Mn",
        "Fe",
        "Co",
        "Ni",
        "Cu",
        "Zn",
        "Ga",
        "Ge",
        "As",
        "Se",
        "Br",
        "Kr",
        "Rb",
        "Sr",
        "Y",
        "Zr",
        "Nb",
        "Mo",
        "Tc",
        "Ru",
        "Rh",
        "Pd",
        "Ag",
        "Cd",
        "In",
        "Sn",
        "Sb",
        "Te",
        "I",
        "Xe",
        "Cs",
        "Ba",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Pm",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Hf",
        "Ta",
        "W",
        "Re",
        "Os",
        "Ir",
        "Pt",
        "Au",
        "Hg",
        "Tl",
        "Pb",
        "Bi",
        "Po",
        "At",
        "Rn",
        "Fr",
        "Ra",
        "Ac",
        "Th",
        "Pa",
        "U",
        "Np",
        "Pu",
        "Am",
        "Cm",
        "Bk",
        "Cf",
        "Es",
        "Fm",
        "Md",
        "No",
        "Lr",
        "Rf",
        "Db",
        "Sg",
        "Bh",
        "Hs",
        "Mt",
        "Ds",
        "Rg",
        "Cn",
        "Fl",
        "Lv",
    ]:
        raise SyntaxFel("Okänd atom vid radslutet " + str(kö))
    else:
        return bok


def regel_första_bok(kö):
    bok = kö.peek()
    if bok is None:
        raise SyntaxFel("Felaktig gruppstart vid radslutet " + str(kö))
    elif bok in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return kö.dequeue()
    elif bok in "abcdefghijklmnopqrstuvwxyz":
        raise SyntaxFel("Saknad stor bokstav vid radslutet " + str(kö))
    else:
        raise SyntaxFel("Felaktig gruppstart vid radslutet " + str(kö))


def regel_andra_bok(kö):
    bok = kö.dequeue()
    if bok in "abcdefghijklmnopqrstuvwxyz":
        return bok
    else:
        raise SyntaxFel("Saknad stor bokstav vid radslutet")


def regel_nummer(kö):
    num = kö.peek()
    if num == "0":
        kö.dequeue()
        raise SyntaxFel("För litet tal vid radslutet " + str(kö))
    elif num not in "0123456789":
        raise SyntaxFel("Saknad siffra vid radslutet " + str(kö))
    total_sum = "0"
    while kö.peek() in "0123456789":
        num = kö.dequeue()
        total_sum += num
        if kö.peek() is None:
            break
    if int(total_sum) >= 2:
        return int(total_sum)
    else:
        raise SyntaxFel("För litet tal vid radslutet " + str(kö))


def lagra_molekyl(molekyl):
    kö = LinkedQ()
    for bokstav in molekyl:
        kö.enqueue(bokstav)
    return kö


def kolla_syntax(molekyl):
    kö = lagra_molekyl(molekyl)
    try:
        mol = regel_formel(kö)
        mg = Molgrafik()
        mg.show(mol)
        input('...')
        return "Formeln är syntaktiskt korrekt"
    except SyntaxFel as fel:
        if str(fel) == "Saknad stor bokstav vid radslutet ":
            return str(fel) + str(molekyl)
        else:
            return str(fel)


def main():
    molekyl = sys.stdin.readline().strip()
    while molekyl != "#":
        print(kolla_syntax(molekyl))
        molekyl = sys.stdin.readline().strip()


"""
    molekyl = input("Ange en molekyl: ")
    print(kolla_syntax(molekyl))
"""

if __name__ == "__main__":
    main()
