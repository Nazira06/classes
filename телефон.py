class Phone:
    def __init__(self, name, model, color, year, state ):
        self.name = name
        self.model = model
        self.color = color
        self.year = year
        self.state = state
        self.memory = 32
        self.price = 1000
        self.battery = 0
        self.touchid = 5
        self.locked = False
    def description(self):
        print(self.name, self.model, self.color, self.year, self.state, self.price, self.battery, self.touchid)
    def set_battery(self,charge):
        if not self.locked:
            if 0<charge<=100:
                self.battery = charge
            else:
                print('Не балуйся!')
    def unlock(self,tries):
        if 0<tries<=self.touchid:
            print("Вы зашли")
        else:
            self.locked = True
            print("Телефон блокирован!Попробуйте через 30 сек")
iphone = Phone('Iphone', 'XII PRO MAX', 'pink', 2019, 'new')
iphone.price = 1100
iphone.unlock(6)
iphone.set_battery(100)
iphone.description()