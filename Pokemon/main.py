class Pokemons:
    def __init__(
        self,
        name,
        type_1,
        type_2,
        total,
        HP,
        attack,
        defense,
        sp_atk,
        sp_def,
        speed,
        generation,
        legendary,
    ):
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2
        self.total = total
        self.HP = HP
        self.attack = attack
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.generation = generation
        self.legendary = legendary

    def __str__(self):
        return f"Pokemon name: {self.name} Attack: {self.attack} HP: {self.HP}"

    def get_name(self):
        return self.name

    def __lt__(self, obj):
        return self.total < obj.total

    def add_attack(self):
        self.attack = str(int(self.attack) + 10)

    def double_HP(self):
        self.HP = str(int(self.HP) * 2)

    def switch_HP_attack(self):
        self.HP, self.attack = self.attack, self.HP


def test_method(
    name,
    type_1,
    type_2,
    total,
    HP,
    attack,
    defense,
    sp_atk,
    sp_def,
    speed,
    generation,
    legendary,
):
    return Pokemons(
        name,
        type_1,
        type_2,
        total,
        HP,
        attack,
        defense,
        sp_atk,
        sp_def,
        speed,
        generation,
        legendary,
    )


def poke_create_list():
    file = open("pokedata.csv", "r")
    data = [i.strip().split(",") for i in file]
    return [
        Pokemons(
            j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8], j[9], j[10], j[11], j[12]
        )
        for j in data
    ]


def poke_search(name, list):
    for i in range(1, len(list)):
        if list[i].get_name() == name:
            return print("Index: " + str(i))
    else:
        return print("Not found")


poke_search("Bulbasaur", poke_create_list())
