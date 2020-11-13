class Marvel:
    def __init__(self, name, type ):
        self.name = name
        self.type = type
        self.power = 'strong'
        self.vulnerability = 0
        self.healht = 100
        self.live = True
        self.god = True
        self.parents = True
        self.sex = ''
        self.attack = 0
    def description(self):
            print(f'имя бога,богини - {self.name}, тип - {self.type}, сила - {self.power}, '
                  f'уязвимость -{self.vulnerability}, здоровье - {self.healht}, жизнь - {self.live}, '
                  f'Бог - {self.god}, родители - {self.parents}, пол - {self.sex}')
class Tor(Marvel):
    def __init__(self, type, lightning, hammer,attack,  name='Tor'):
        super(). __init__(name, type)
        self.lightning = lightning
        self.hammer = hammer
        self.attack = attack
    def description(self):
            print(f'имя бога,богини - {self.name}, тип - {self.type}, сила - {self.power}, '
                  f'уязвимость -{self.vulnerability}, здоровье - {self.healht}, жизнь - {self.live}, '
                  f'Бог - {self.god}, родители - {self.parents}, пол - {self.sex}, Особенность - {self.lightning},'
                  f' Особенность2 - {self.hammer}' )

class Hela(Marvel):
    def __init__(self, type,teleportation ,black_magic , attack, name='Hela'):
        super().__init__(name, type)
        self.black_magic = black_magic
        self.teleportation = teleportation
        self.attack = attack
    def description(self):
        print(f'имя бога,богини - {self.name}, тип - {self.type}, сила - {self.power}, '
              f'уязвимость -{self.vulnerability}, здоровье - {self.healht}, жизнь - {self.live}, '
              f'Бог - {self.god}, родители - {self.parents}, пол - {self.sex}, Особенность - {self.black_magic},'
              f' Особенность2 - {self.teleportation} ')

class Fight():
    def __init__(self, healht, attack):
        self.heals = healht
        self.attack = attack
    def __add__(self, other):
        fam = self.heals - other.attack
        return fam




hela1 = Hela('evil', 'black magic', 'teleportation', 11)
hela1.sex = 'famale'
tor2 = Tor('good', 'lightning', 'hammer', 10)
tor2.sex = 'male'
hela1.description()
tor2.description()
tor = Fight(tor2.healht, hela1.attack)
hela = Fight(hela1.healht, tor2.attack)
while tor2.healht > 0 or hela1.healht >0:
    fam1 = tor + hela
    fam2 = hela + tor
    print(f'удар Хелы - {fam2}, удар Тора - {fam1}, Здоровье Хелы - {hela1.healht}, Здоровье Тора {tor2.healht}')
