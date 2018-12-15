## @file Colors.py
#  @author Andy Hameed
#  @brief Define color constants
#  @date 11/09/2018

import pygame
from random import randint

#initializing PyGame and setting game window dimensions
pygame.init()
screenSize = 500
win = pygame.display.set_mode((screenSize,screenSize))
pygame.display.set_caption("Snake")

# One size for all blocks created for snake
size = 20
grid_length = screenSize/size

#make initial position sit within the grid
x = randint(0, grid_length) * size
y = randint(0, grid_length) * size
