class Airplane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False
        # self.land = True
    def take_off(self, is_flying):
        self.is_flying == True
        # self.land = False
    def land (self, is_flying):
        self.land == False

    def fly(self, km):
        self.odometer = self.odometer + km

    def print_arg(self):
        print(self.make, self.model, self.year, self.max_speed)

Airplane1 = Airplane("Boing", "sc1", "2009", "600")
Airplane1.print_arg()
Airplane1.take_off(True)
Airplane1.land(False)
Airplane1.fly(1000)
print(Airplane1.odometer)




