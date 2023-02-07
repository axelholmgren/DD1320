from bintreeFile import Bintree
from linkedQFile import LinkedQ

svenska = Bintree()  # Skapar ett tomt träd för svenska ord
with open("/Users/axelholmgren/GitHub/DD1320/Laboration_4/word3.txt", "r", encoding="utf-8") as svenskfil:  # Läser in filen
    for rad in svenskfil:
        ordet = rad.strip()  # Ett trebokstavsord per rad
        svenska.put(ordet)  # in i sökträdet

gamla = Bintree()  # Skapar ett tomt träd för gamla ord
for ord in rad.split():
    if (ord.strip() in svenska and ord.strip() not in gamla):  # kollar om det finns i svenska trädet men inte i gamlaträdet
        gamla.put(ord.strip())  # Lägger till i gamlaträdet

# Funktion som skapar barn, tar in startord, kön och slutord. Ett barn skiljer endast med en bokastav från förälder.
def makechildren(startord, q, slutord):
    gamla.put(startord) # Lägger till startordet som root.
    for i in range(3): # indexerar för varje bokstav
        ord_list = list(startord.strip()) 
        for j in "abcdefghijklmnopqrstuvwxyzåäö": # Lägger in en ny bokstav på den nuvarande postionen i ordet.
            ord_list[i] = j 
            ord = "".join(ord_list) # lägger ihop till en sträng
            if ord in svenska and ord not in gamla: # Om ordet finns i svenska men inte i gamlaträdet. Om något av argumenten inte är upppfyllda läggs ordet in i gamla och lägger in i kön sist 
                if ord == slutord:
                    print("Det finns en väg till", slutord) 
                    return True # Retrunerar true för att avsluta sökningen.
                else:
                    gamla.put(ord)
                    q.enqueue(ord)
    return False

# Genomför en breddenförstsökning för att hitta den kortaste vägen och skriver ut om det finns en väg eller inte. Tar in avnändarinput.
def main():
    startord = input(str("Ange ett startord: "))
    slutord = input(str("Ange ett slutord: "))
    q = LinkedQ() # Skapar en tom kö
    q.enqueue(startord) # Lägger till startordet i kön
    while not q.isEmpty(): # Medans kön inte är tom, skapar en ny nod
        nod = q.dequeue()
        if makechildren(nod, q, slutord): # Om makechildren returnerar true har en väg hittats, om false forsätt skapa nya barn och fortsätt sökningen 
            return None # returnerar None för att bryta loopen
    print("Det finns ingen väg till", slutord)

main()
