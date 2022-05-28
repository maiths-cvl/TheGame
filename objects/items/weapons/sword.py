from objects.items.weapons.weapon import *

class Sword(Weapon):
    def __init__(self, x, y, name, lore, type, attackDmg, durabiliy, attackSpeed, texture):
        super().__init__(x, y, name, lore, type, attackDmg, durabiliy, texture)
        self.attackSpeed = attackSpeed # hit per secondes