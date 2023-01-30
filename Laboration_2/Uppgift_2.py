from bintreeFile import Bintree
svenska = Bintree()
with open("/Users/axelholmgren/GitHub/DD1320/Laboration_2/word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end = " ") 
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")