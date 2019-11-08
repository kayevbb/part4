class Soldier:
    def __init__(self, name, gun_type):
        self.name = name
        self.gun_type = gun_type
        print(name, 'has an', gun_type)

class Gun(Soldier):
    def gun(self):
        Soldier.init(self, name, gun_type)
        self.bullets = 12
        print('Оружие заряжено:', self.bullets, 'патроны')

    def fire_bullets(self):
        self.bullets = 0
        print('Оружие перезаряжено:', self.bullets, 'патроны')

    def reload_bullets(self, bullets):
        self.bullets += bullets
        print('Оружие было перезаряжено:', self.bullets, 'патроны')

class Act_of_shooting(Gun):
    def init(self, name, gun_type):
        Gun.init(self, name, gun_type)

soldier = Act_of_shooting('Ryan', 'AK47')
soldier.fire_bullets()
soldier.reload_bullets(15)
soldier.fire_bullets()
soldier.reload_bullets(7)
soldier.fire_bullets()
