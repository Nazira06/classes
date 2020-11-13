class Planet:
    def __init__(self, name, position):
        self.name = name
        self.form = 'shape'
        self.position = position
        self.temp = 0
        self.size = 0
    def description(self):
        print(self.name, self.position, self.form, self.temp, self.size)

class Mercury(Planet):
    def __init__(self, position, name = 'Mercury'):
        super(). __init__(name, position)
        self.temp = 120
        self.size = 'small'
class Jupiter(Planet):
    def __init__(self, position, name = 'Jupiter'):
        super().__init__(name, position)
        self.temp = 120
        self.size = 'big'
        self.diamond_rain = True

    def description(self):
        print(self.name, self.position, self.form, self.temp, self.size, self.diamond_rain)

class Saturn(Planet):
    def __init__(self, position, name='Saturn'):
        super().__init__(name, position)
        self.temp = 120
        self.size = 'big'
        self.rings = True
        self.count_rings = 7

    def description(self):
        print(self.name, self.position, self.form, self.temp, self.size, self.count_rings, self.rings)
small_planet = Mercury('solar system')
small_planet.description()
big_planet = Jupiter('solar system')
big_planet.description()
rings_planet = Saturn('solar system')
rings_planet.description()
