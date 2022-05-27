from utils.getfromconfig import *
from utils.onStart import *
from utils.allGame import *
from utils.writecfg import *
import os
import pygame
from configparser import ConfigParser

pygame.init()

WIDTH, HEIGHT = 1080, 720
MAXFPS = 144

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

config = ConfigParser()
config.read("options.cfg")
key = config['options']['maxfps']
print(key)

DATADIR = config['options']['datapath']

listofdir = ['data/', 'data/PLAYER/', 'data/PLAYER/inventory/']
listoffiles = ['data/PLAYER/inventory/invenoty.cfg', 'data/PLAYER/inventory/state.cfg']

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The game i'm creating right now but idk the name so shut up")

# initalize here bro plz

playerdircheck(DATADIR, listofdir)
playerfilescheck(DATADIR, listoffiles)

listincfg = ['time = 12', 'ball = 1205', 'me = perfect']

writeIn('options.cfg', listincfg)

clock = pygame.time.Clock()
run = True

while run:

    clock.tick(MAXFPS)
    screen.fill(WHITE)

    allGameCheck(DATADIR, listofdir)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()

    
    pygame.display.update()
