## @file Snake.py
#  @author Andy Hameed
#  @brief implements an abstract data type for a snake
#  @date 11/09/2018

from random import randint
from init import *

## @brief An Abstract Data type representing a snake character object
class Snake():

    ## @brief Snake constructor
    #  @details Initializes a Snake object with its initial attributes
    #  @param blockSize the width and height of the square block representing the snake 
    #  @param direct The direction of the snake's movement
    #  @param speed The initial speed of the snake's movement
    def __init__(self, blockSize, direct, speed, axis):
        self.speed = speed
        self.direct = direct
        self.size = blockSize
        self.axis = axis

    ## @brief Draw method uses pygame to draw the snake object
    #  @param x The x-coordinate where the block should be drawn 
    #  @param y The y-coordinate where the block should be drawn
    def draw(self,colour, snake_loc):
        for x,y in snake_loc:
            pygame.draw.rect(win, colour , [x,y, self.size, self.size])

  

        
