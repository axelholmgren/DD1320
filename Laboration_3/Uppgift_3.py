from bintreeFile import Bintree


svenska = Bintree()                                                                                                 # Skapar ett tomt träd för svenska ord
with open("/Users/axelholmgren/GitHub/DD1320/Laboration_3/word3.txt", "r", encoding = "utf-8") as svenskfil:        # Läser in filen
    for rad in svenskfil:                                                                                           
        ordet = rad.strip()                                                                                          # Ett trebokstavsord per rad
        svenska.put(ordet)                                                                                           # in i sökträdet

engelska = Bintree()                                                                                                 # Skapar ett tomt träd för engelska ord
with open("/Users/axelholmgren/GitHub/DD1320/Laboration_3/engelska.txt", "r", encoding = "utf-8") as engelskafil:    # Läser in filen
    for rad in engelskafil: 
        for word in rad.split():                                                                                     
            if word.strip() in svenska and word.strip() not in engelska:                                             # kollar om det finns i svenska trädet men inte i engelskaträdet
                print(word.strip(), end = " ")                                                                       # Skriver ut ordet
            engelska.put(word.strip())                                                                               # Lägger till i engelskaträdet
