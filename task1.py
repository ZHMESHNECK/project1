class Home:
    def __init__(self):
        self.temperature = 25
        
    def add(self):
        self.temperature -= 5
        print(self.temperature)

    def min(self):
        self.temperature += 5
        print(self.temperature)

a = Home()
a.add()
a.add()
a.add()