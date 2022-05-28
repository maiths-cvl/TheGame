from turtle import position
from objects.entities.entity import Entity
import pygame

class Player(Entity):
    def __init__(self, name, level, slot, health, maxhealth, food, maxfood, walkspeed, attackDmg, defence, x, y):
        super().__init__(level, health, maxhealth, food, maxfood, walkspeed, attackDmg, defence, x, y)
        self.name = name
        self.slot = slot # i think player will have 36 slot
        self.inventory = self.readInv()

        

        self.images = {
            'down': self.getImage(0, 0),
            'left': self.getImage(0, 32),
            'right': self.getImage(0, 64),
            'up': self.getImage(0, 96)
        }
        
    def changeAnimation(self, name):
        self.image = self.images[name]
        self.image.set_colorkey([0, 0, 0])

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

    def handleInput(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_z]:
            self.position[1] -= self.walkspeed
            self.changeAnimation("up")
        if pressed[pygame.K_s]:
            self.position[1] += self.walkspeed
            self.changeAnimation("down")
        if pressed[pygame.K_d]:
            self.position[0] += self.walkspeed
            self.changeAnimation("right")
        if pressed[pygame.K_q]:
            self.position[0] -= self.walkspeed
            self.changeAnimation("left")