from PokeClassFile import Pokemons

# from DictHash import DictHash
from HashTable import Hashtable


def poke_create_table():  # /Dicthash beroende på vilken klass man vill använda
    file = open("/Users/axelholmgren/GitHub/DD1320/Laboration_7/pokedata.csv", "r")
    data = [i.strip().split(",") for i in file]
    table = Hashtable(len(data))
    for j in data:
        table.store(
            j[1],
            Pokemons(j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8], j[9], j[10], j[11], j[12]),
        )
    return table


def main():
    table = poke_create_table()
    print(table.crash)
    print(table.search(input("Pokemon namn: ")))


main()
