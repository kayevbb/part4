class House:
    def __init__(self, household_type, total_area):
        self.type = household_type
        self.total_area = total_area
        self.furniture = []
        print("Свободная площадь дома: ", self.total_area, 'sq m.', end='  ')
        print('Мебель дома: ', self.furniture, '\n')

    def add_furniture(self, name, area):
        self.name = name
        self.area = area
        self.total_area = self.total_area - self.area
        self.furniture.append(name)
        print(name, 'Купили')
        print("\nСвободная площадь дома: ", house.total_area, 'sq m.', end='  ')
        print('Мебель дома: ', house.furniture)


house = House('Mansion', 24)
house.add_furniture('диван', 8)
house.add_furniture('Шкаф', 2)
house.add_furniture('стол', 9)
