class Game:
    def __init__(self, player):
        self.player = player
        self.ships = 4
        self.position1 = 0
        self.position2 = 0
        self.position3 = 0
        self.position4 = 0

    def player_attack(self,attack_position):
        if self.position1 == attack_position or self.position2 == attack_position or self.position3 == attack_position or self.position4 == attack_position:
            print('Попал! Выбирайте новую цель!')