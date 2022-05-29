import pygame
from objects.items.items import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, level, health, maxhealth, food, maxfood, walkspeed, attackDmg, defence, x ,y):
        super().__init__()
        self.level = level
        self.health = health
        self.maxhealth = maxhealth
        self.food = food
        self.maxfood = maxfood
        self.walkspeed = walkspeed / 10
        self.attackDmg = attackDmg
        self.defence = defence
        self.position = [x, y]

        self.itemInHand = None

        self.life = True

        self.sprite_sheet = pygame.image.load('assets/player/player2.png')
        self.image = self.getImage(0, 0)
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()

        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()

    def saveLocation(self):
        self.old_position = self.position.copy()

    def getImage(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image

    def update(self):
        if self.health <= 0:
            self.life = False
            print("you died")
        if self.health > 0:
            self.life = True
            #print(str(self) + " is living")

        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def moveBack(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def attack(self, target):
        if type(target) == list:
            for i in target:
                if type(i) == Entity or type(i):
                    i.hit(self.attackDmg)
        elif type(target) == Entity or type(i):
            target.hit(self.attackDmg)

    def hit(self, damage):
        self.health -= (damage / (1 + (self.defence / 10)))
