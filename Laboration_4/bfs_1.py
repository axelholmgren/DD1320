from bintreeFile import Bintree

svenska = Bintree()  # Skapar ett tomt träd för svenska ord
with open(
    "/Users/axelholmgren/GitHub/DD1320/Laboration_4/word3.txt", "r", encoding="utf-8"
) as svenskfil:  # Läser in filen
    for rad in svenskfil:
        ordet = rad.strip()  # Ett trebokstavsord per rad
        svenska.put(ordet)  # in i sökträdet

gamla = Bintree()  # Skapar ett tomt träd för gamla ord
for ord in rad.split():
    if (
        ord.strip() in svenska and ord.strip() not in gamla
    ):  # kollar om det finns i svenska trädet men inte i gamlaträdet
        pass
    gamla.put(ord.strip())  # Lägger till i gamlaträdet


def makechildren(startord):
    gamla.put(startord)
    for i in range(3):
        ord_list = list(startord.strip())
        for j in "abcdefghijklmnopqrstuvwxyzåäö":
            ord_list[i] = j
            ord = "".join(ord_list)
            if ord in svenska and ord not in gamla:
                print(ord)
                gamla.put(
                    ord
                )


def main():
    startord = input(str("Ange ett startord: "))
    slutord = input(str("Ange ett slutord: "))
    makechildren(startord)


main()
