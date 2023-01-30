from bintreeFile import Bintree


svenska = Bintree()
with open("/Users/axelholmgren/GitHub/DD1320/Laboration_2/word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        svenska.put(ordet)                 # in i sökträdet

engelska = Bintree()
with open("/Users/axelholmgren/GitHub/DD1320/Laboration_2/engelska.txt", "r", encoding = "utf-8") as engelskafil:
    for rad in engelskafil:
        for word in rad.split():
            if word.strip() in svenska and word.strip() not in engelska:
                print(word.strip(), end = " ")
            engelska.put(word.strip())
