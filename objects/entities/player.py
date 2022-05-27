from objects.entities.entity import Entity
import pygame

class Player(Entity):
    def __init__(self, name, level, slot, health, maxhealth, food, maxfood, walkspeed, attackDmg, defence):
        super().__init__(level, health, maxhealth, food, maxfood, walkspeed, attackDmg, defence)
        self.name = name
        self.slot = slot # i think player will have 36 slot
        self.inventory = self.readInv()
        

    def saveInventory(self, stuff):
        self.inventory = stuff

        with open('data/PLAYER/inventory/inventory.txt', "w+") as file:
            for i in stuff:
                file.write(str(i) + ";")
            file.close()

    def readInv(self):
        with open('data/PLAYER/inventory/inventory.txt', "r+") as file:
            listof = file.read()
            listof = listof.split(';')
            listof.remove('')
            return listof

    def playerUpdate(self):
        self.inventory = self.readInv()