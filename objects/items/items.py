import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, name, lore, type, texture):
        super().__init__()
        self.name = name
        self.lore = lore
        self.type = type

        self.position = [x, y]

        self.sprite_sheet = pygame.image.load(texture)
        self.image = self.getImage(0, 0)
        # self.image = pygame.transform.scale(self.image, (32, 32)) resize the picture
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()

    def getImage(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image

    def getHanded(self, other):
        self.position = [other.position[0] + 20, other.position[1] - 4]

    def update(self):
        self.rect.topleft = self.position

    