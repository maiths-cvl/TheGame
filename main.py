from utils.getfromconfig import *
import pygame

pygame.init()

WIDTH, HEIGHT = 1080, 720
MAXFPS = 144


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The game i'm creating right now but idk the name so shut up")

clock = pygame.time.Clock()
run = True

while run:

    clock.tick(MAXFPS)
    
    pygame.display.update()
