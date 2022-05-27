from objects.entities.entity import *
from objects.entities.player import *
from utils.getfromconfig import *
from utils.onStart import *
from utils.allGame import *
from utils.writecfg import *
import os
import pygame
from configparser import ConfigParser
import pytmx
import pyscroll

pygame.init()

WIDTH, HEIGHT = 800, 800
MAXFPS = 144

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

ENTITYTYPELIST = [Entity, Player]

config = ConfigParser()
config.read("options.cfg")
key = config['options']['maxfps']
print(key)

DATADIR = config['options']['datapath']

listofdir = ['data/', 'data/PLAYER/', 'data/PLAYER/inventory/', 'data/world/', 'data/world/environement/', 'data/world/enities/']
listoffiles = ['data/PLAYER/inventory/inventory.txt', 'data/PLAYER/inventory/state.cfg']

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The game i'm creating right now but idk the name so shut up")

tmx_data = pytmx.util_pygame.load_pygame('data/world/environement/map.tmx')

map_data = pyscroll.data.TiledMapData(tmx_data)
map_layer = pyscroll.orthographic.BufferedRenderer(map_data, screen.get_size())
map_layer.zoom = 2

# dessiner le groupe de calque
group = pyscroll.PyscrollGroup(map_layer=map_layer, delfault_layer=1)

# initalize here bro plz

playerdircheck(DATADIR, listofdir)
playerfilescheck(DATADIR, listoffiles)

#slistincfg = ['time = 12', 'ball = 1205', 'me = perfect']

#writeIn('options.cfg', listincfg)


me = Player("CVL", 1, 36, 20, 20, 20, 20, 10, 15, 20)
print(me.inventory)

stuff = ['one', 'two', 'three', 'four']
me.saveInventory(stuff)
me.inventory = me.readInv()
print(me.inventory)



otherone = Entity(1, 20, 20, 20, 20, 10, 15, 20)
othertwo = Entity(1, 20, 20, 20, 20, 10, 15, 20)

entityalive = [me, otherone, othertwo]

group.add(me)

clock = pygame.time.Clock()
run = True

while run:

    clock.tick(MAXFPS)
    screen.fill(WHITE)

    allGameCheck(DATADIR, listofdir)
    
    for i in entityalive:
        i.update()

    group.draw(screen)

    me.playerUpdate()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            # before exit
            me.saveInventory(me.inventory)
            print("inventory saved")

            run = False
            quit()

    
    pygame.display.update()
