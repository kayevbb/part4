print('Сколько километров Вы хотите проехать?')
num = int(input())
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 70

    def drive(self, km):
        if km <= 700:
            self.__add_distance(km)
            self.__subtract_fuel(km)
            print("Поехали!!\n")

        else:
            print("Не хвататет бензина!\n")

    def __add_distance(self, km):
        self.odometer += km

    def __subtract_fuel(self, km):
        km = km/10
        self.fuel -= km

new_car = Car("Mercedes", "e class", 2017)
print("\nДо езды: ", new_car.odometer, 'km')
print("До езды: ", new_car.fuel, 'l', '\n')
new_car.drive(num)
print("После езды: ", new_car.odometer, 'km')
print("После езды", new_car.fuel, 'l')


