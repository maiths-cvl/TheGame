from utils.getfromconfig import *
from utils.onStart import *
import os
import pygame

pygame.init()

WIDTH, HEIGHT = 1080, 720
MAXFPS = 144

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

DATADIR = "C:/Users/capit/Desktop/Python/data/PLAYER/"

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The game i'm creating right now but idk the name so shut up")

# initalize here bro plz

playerdircheck(DATADIR)

clock = pygame.time.Clock()
run = True

while run:

    clock.tick(MAXFPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()

    
    pygame.display.update()
