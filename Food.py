## @file Food.py
#  @author Usman Irfan
#  @brief implements an abstract data type for a snake's food
#  @date 11/09/2018

from random import randint
from init import *

## @brief An Abstract Data type which represents a one-unit of food
class Food():


    ## @brief Food constructor
    #  @details Initializes the size of the food, this needs to be the same as 
    #   snake's block size
    #  @param blockSize the width and height of the square block representing the food
    def __init__(self, blockSize):
        self.size = blockSize

    ## @brief Draw method uses pygame to draw the food object on the window
    #  @param location A list which consists the x and y location of the food
    def draw_food(self, food_colour, location):
        maze_x = (location[0] == 100)
        maze_y = location[1] >= 100 and location[1] <= 320
        maze2_x = (location[0] == 380)
        if ((maze_x and maze_y) or (maze2_x and maze_y)):
                location[0] = randint(0, grid_length - 1) * self.size
                location[1] = randint(0, grid_length - 1) * self.size
        pygame.draw.rect(win, food_colour , (location[0],location[1], self.size, self.size))

    ## @brief redraw_food method redraws the food on the screen randomly
    #  @param x is the location of snake's x-axis head location
    #  @param y is the location of snake's y-axis head location
    #  @param location is a list that gives the location of present food
    #  @param screenSize is the size of the screen
    def redraw_food(self, x, y, location,screenSize, snake_loc):
        maze_x = (x == 100)
        maze_y = y >= 100 and y <= 320
        maze2_x = (x == 380)
        
        if(abs(x - location[0]) < 15 and abs(y - location[1]) < 15):
            location[0] = randint(0, grid_length - 1) * self.size
            location[1] = randint(0, grid_length - 1) * self.size
            if((location in snake_loc) or (maze_x and maze_y) or (maze2_x and maze_y)):
               location[0] = randint(0, grid_length - 1) * self.size
               location[1] = randint(0, grid_length - 1) * self.size
            
