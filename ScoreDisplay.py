## @file ScoreDisplay.py
#  @author Vaibhav Chadha
#  @brief implements the interface after the snake dies
#  @date 11/22/2018

import pygame, sys
import highscore, Interface, Gameplay
import GUI
from colors import *

def storeScore(score):
    prevScore = int(highscore.HighScore.findHighScore())
    if(score > prevScore):
        infile = open("highscore.txt", "w")
        infile.write(str(score))
    else: return

def display(score,speed, colour,food_colour, backgroundColour):
    pygame.init()
    storeScore(score)
    image1 = pygame.image.load("Images/Exit_image.png")

    
    run = True
    while run:

        mousepos = pygame.mouse.get_pos() #checking mouse position
        mouseclick = pygame.mouse.get_pressed()#checking mouse pressed
        lastPage = pygame.display.set_mode((500, 500))
        lastPage.blit(image1,(0,0))

        GUI.custom_text('Your Score is ' + str(score),"Roboto-Light.ttf", 40,black,(93,50),lastPage)

        if (150 <= mousepos[0] <= 150+200 and 150 <= mousepos[1] <= 150+60 ):
            GUI.button(lastPage,darkgray, [150,150,200,60], 0)
            if mouseclick[0] == 1:
                Gameplay.game(speed, colour,food_colour, backgroundColour)
        else:
            GUI.button(lastPage,lightBlue, [150,150,200,60], 0)
        GUI.custom_text('Play Again',"Roboto-Light.ttf", 25, white,(193,165),lastPage)

        if (150 <= mousepos[0] <= 150+200 and 260 <= mousepos[1] <= 260+60 ):
            GUI.button(lastPage,darkgray, [150,260,200,60], 0)
            if mouseclick[0] == 1:
                Interface.main()
        else:
            GUI.button(lastPage,lightBlue, [150,260,200,60], 0)
        GUI.custom_text('Main Menu',"Roboto-Light.ttf", 25,white,(189,275),lastPage)
        
        if (150 <= mousepos[0] <= 150+200 and 370 <= mousepos[1] <= 370+60 ):
            GUI.button(lastPage,darkgray, [150,370,200,60], 0)
            if mouseclick[0] == 1:
                pygame.quit()
                sys.exit()
        else:
            GUI.button(lastPage,lightBlue, [150,370,200,60], 0)
        GUI.custom_text('Quit',"Roboto-Light.ttf", 25,white,(225,385),lastPage)
            
        pygame.display.update()
