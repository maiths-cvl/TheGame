from objects.items.items import *

class Weapon(Item):
    def __init__(self, x, y, name, lore, type, attackDmg, durabiliy, texture):
        super().__init__(x, y, name, lore, type, texture)
        self.attackDmg = attackDmg
        self.durability = durabiliy