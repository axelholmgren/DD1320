import sys
from LinkedQueue import LinkedQ


class SyntaxFel(Exception):
    pass


def regel_molekyl(kö):
    regel_atom(kö)
    if kö.isEmpty() is False:
        regel_nummer(kö)


def regel_atom(kö):
    regel_första_bok(kö)
    if kö.peek() is None:
        return
    elif kö.peek() in "0123456789":
        return
    else:
        regel_andra_bok(kö)


def regel_första_bok(kö):
    bok = kö.dequeue()
    if bok in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return
    else:
        raise SyntaxFel("Saknad stor bokstav vid radslutet ")


def regel_andra_bok(kö):
    bok = kö.dequeue()
    if bok in "abcdefghijklmnopqrstuvwxyz":
        return
    else:
        raise SyntaxFel("Saknad stor bokstav vid radslutet")


def regel_nummer(kö):
    num = kö.dequeue()
    sum = "0"
    while num in "0123456789":
        sum += num
        if kö.peek() is None or int(sum[1]) == 0:
            break
        num = kö.dequeue()
    if int(sum) >= 2:
        return
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
        regel_molekyl(kö)
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
