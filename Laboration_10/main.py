import sys
from LinkedQueue import LinkedQ
from molgrafik import *
from rutaclassFile import Ruta

dev


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
        rutan.atom, rutan.weight = regel_atom(kö)
        if kö.isEmpty() is False:
            if kö.peek() in "0123456789":
                rutan.num = regel_nummer(kö)
    return rutan


def regel_atom(kö):
    bok = regel_första_bok(kö)
    if kö.isEmpty() is False and kö.peek() in "abcdefghijklmnopqrstuvwxyz":
        bok += str(regel_andra_bok(kö))
    for rad in [
        "H,1.00794",
        "He,4.002602",
        "Li,6.941",
        "Be,9.012182",
        "B,10.811",
        "C,12.0107",
        "N,14.0067",
        "O,15.9994",
        "F,18.9984032",
        "Ne,20.1797",
        "Na,22.98976928",
        "Mg,24.3050",
        "Al,26.9815386",
        "Si,28.0855",
        "P,30.973762",
        "S,32.065",
        "Cl,35.453",
        "K,39.0983",
        "Ar,39.948",
        "Ca,40.078",
        "Sc,44.955912",
        "Ti,47.867",
        "V,50.9415",
        "Cr,51.9961",
        "Mn,54.938045",
        "Fe,55.845",
        "Ni,58.6934",
        "Co,58.933195",
        "Cu,63.546",
        "Zn,65.38",
        "Ga,69.723",
        "Ge,72.64",
        "As,74.92160",
        "Se,78.96",
        "Br,79.904",
        "Kr,83.798",
        "Rb,85.4678",
        "Sr,87.62",
        "Y,88.90585",
        "Zr,91.224",
        "Nb,92.90638",
        "Mo,95.96",
        "Tc,98",
        "Ru,101.07",
        "Rh,102.90550",
        "Pd,106.42",
        "Ag,107.8682",
        "Cd,112.411",
        "In,114.818",
        "Sn,118.710",
        "Sb,121.760",
        "I,126.90447",
        "Te,127.60",
        "Xe,131.293",
        "Cs,132.9054519",
        "Ba,137.327",
        "La,138.90547",
        "Ce,140.116",
        "Pr,140.90765",
        "Nd,144.242",
        "Pm,145",
        "Sm,150.36",
        "Eu,151.964",
        "Gd,157.25",
        "Tb,158.92535",
        "Dy,162.500",
        "Ho,164.93032",
        "Er,167.259",
        "Tm,168.93421",
        "Yb,173.054",
        "Lu,174.9668",
        "Hf,178.49",
        "Ta,180.94788",
        "W,183.84",
        "Re,186.207",
        "Os,190.23",
        "Ir,192.217",
        "Pt,195.084",
        "Au,196.966569",
        "Hg,200.59",
        "Tl,204.3833",
        "Pb,207.2",
        "Bi,208.98040",
        "Po,209",
        "At,210",
        "Rn,222",
        "Fr,223",
        "Ra,226",
        "Ac,227",
        "Pa,231.03588",
        "Th,232.03806",
        "Np,237",
        "U,238.02891",
        "Am,243",
        "Pu,244",
        "Cm,247",
        "Bk,247",
        "Cf,251",
        "Es,252",
        "Fm,257",
        "Md,258",
        "No,259",
        "Lr,262",
        "Rf,265",
        "Db,268",
        "Hs,270",
        "Sg,271",
        "Bh,272",
        "Mt,276",
        "Rg,280",
        "Ds,281",
        "Cn,285",
        "Fl,289",
        "Lv,293",
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
        input("...")
        return "Formeln är syntaktiskt korrekt"
    except SyntaxFel as fel:
        if str(fel) == "Saknad stor bokstav vid radslutet ":
            return str(fel) + str(molekyl)
        else:
            return str(fel)


def weight(mol):
    try:
        return sum_weight(regel_formel(mol))

    except SyntaxFel as fel:
        if str(fel) == "Saknad stor bokstav vid radslutet ":
            return str(fel) + str(mol)
        else:
            return str(fel)


def sum_weight(ruta):
    vikt = 0
    if ruta.down is not None:
        vikt += sum_weight(ruta.down) * int(ruta.num)
    elif ruta.next is not None:
        vikt += sum_weight(ruta.next)
    else:
        vikt = int(ruta.atom) * int(ruta.num)
        return vikt


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
