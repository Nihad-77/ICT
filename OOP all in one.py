class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, dmg):
        self.hp -= dmg


class Warrior(Player):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength

    def attack(self):
        return self.strength * 2


Nihad = Warrior("Nihad", 100, 20)
print(Nihad.attack())
Nihad.take_damage(30)
print(Nihad.hp)
