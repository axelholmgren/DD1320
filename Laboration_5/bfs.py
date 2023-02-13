from bintreeFile import Bintree
from linkedQFile import LinkedQ
from parentnodeFile import ParentNode
from solutionfoundFile import SolutionFound

svenska = Bintree()  # Skapar ett tomt träd för svenska ord
with open("/Users/axelholmgren/GitHub/DD1320/Laboration_4/word3.txt", "r", encoding="utf-8") as svenskfil:  # Läser in filen
    for rad in svenskfil:
        ordet = rad.strip()  # Ett trebokstavsord per rad
        svenska.put(ordet)  # in i sökträdet

gamla = Bintree()  # Skapar ett tomt träd för gamla ord

# Funktion som skapar barn, tar in startord, kön och slutord. Ett barn skiljer endast med en bokastav från förälder.
def makechildren(nod, q, slutord):
    for i in range(3): # indexerar för varje bokstav
        ord_list = list(nod.word.strip()) 
        for j in "abcdefghijklmnopqrstuvwxyzåäö": # Lägger in en ny bokstav på den nuvarande postionen i ordet.
            ord_list[i] = j 
            ord = "".join(ord_list) # lägger ihop till en sträng
            if ord in svenska and ord not in gamla: # Om ordet finns i svenska men inte i gamlaträdet. Om något av argumenten inte är upppfyllda läggs ordet in i gamla och lägger in i kön sist 
                if ord == slutord:
                    print("Vägen till slutordet är: ")
                    writechain(ParentNode(ord, nod))
                    raise SolutionFound 
                else:
                    gamla.put(ord)
                    q.enqueue(ParentNode(ord, nod))

def writechain(slutordsnod):
    if slutordsnod.parent != None:
        writechain(slutordsnod.parent)
    print(slutordsnod.word)


# Genomför en breddenförstsökning för att hitta den kortaste vägen och skriver ut om det finns en väg eller inte. Tar in avnändarinput.
def main():
    while True:
        startord = input(str("Ange ett startord: "))
        if startord in svenska:
            break
        else:
            print("Ordet som angavs är inte giltigt, försök igen: ")
    slutord = input(str("Ange ett slutord: "))
    q = LinkedQ()  # Skapar en tom kö
    gamla.put(startord)
    q.enqueue(ParentNode(startord)) # Lägger till startordet i kön
    try:
        while not q.isEmpty(): # Medans kön inte är tom, skapar en ny nod
            nod = q.dequeue()
            makechildren(nod, q, slutord) # Om makechildren returnerar true har en väg hittats, om false forsätt skapa nya barn och fortsätt sökningen 
        print("Det finns ingen väg till", slutord)
    except SolutionFound:
        pass

main()
