## @file help.py
#  @author Vaibhav Chadha
#  @brief implements the help interface of this game
#  @date 11/09/2018
#importing necessary libraries
x = 10
y = 40
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

import pygame, sys
import Interface
import GUI

def main():
    pygame.init()
    image1 = pygame.image.load("Images/Exit_image_empty.png")
    run = True
    while run:
        help_ = pygame.display.set_mode((500,500))
        help_.blit(image1,(0,0))
        mousepos = pygame.mouse.get_pos() #checking mouse position
        mouseclick = pygame.mouse.get_pressed()#checking mouse pressed
        pygame.display.set_caption("Help")

        GUI.text('Use the following keys for the movement of the snake:','times',20,[130,190,0],(40,30),help_)
        GUI.text('"Up" arrow key for turning Upwards','times',20,[90,190,0],(60,60),help_)
        GUI.text('"Down" arrow key for turning Downwards','times',20,[90,190,0],(60,90),help_)
        GUI.text('"Right" arrow key for turning Rightwards','times',20,[90,190,0],(60,120),help_)
        GUI.text('"Left" arrow key for turning Leftwards','times',20,[90,190,0],(60,150),help_)
        GUI.text('Beginner:','times',20,[200,0,0],(60,190),help_)
        GUI.text('The snake can cross through the boundaries','times',20,[90,190,0],(140,190),help_)
        GUI.text('Intermediate:','times',20,[200,0,0],(60,220),help_)
        GUI.text('The snake will die as it touches the ','times',20,[90,190,0],(165,220),help_)
        GUI.text('boundary.(The speed is faster than beginner)','times',20,[90,190,0],(140,250),help_)
        GUI.text('Advance:','times',20,[200,0,0],(60,280),help_)
        GUI.text('The snake will die as it touches the boundary','times',20,[90,190,0],(140,280),help_)
        GUI.text('or barrier.(Same speed as intermediate)','times',20,[90,190,0],(120,310),help_)
        GUI.text('THEMES','times',20,[0,50,200],(110,340),help_)
        GUI.text('Regular           Dark','times',20,[200,0,0],(220,340),help_)
        GUI.text('Snake','times',20,[200,0,0],(100,370),help_)
        GUI.text('Background','times',20,[200,0,0],(80,400),help_)
        GUI.text('BLUE             WHITE','times',20,[90,190,0],(220,370),help_)
        GUI.text('WHITE           BLACK','times',20,[90,190,0],(220,400),help_)
        
        if (160 <= mousepos[0] <= 160+180 and 440 <= mousepos[1] <= 440+50 ):
        #checks if the mouse is hovering over the button
            GUI.button(help_,[100,100,100], [160,440,180,50], 0)
            #checking if the button is clicked
            if mouseclick[0] == 1:
                Interface.main()         
        else:
            GUI.button(help_,[180,180,180], [160,440,180,50], 0)
        GUI.custom_text('Main Menu',"Roboto-Light.ttf", 30,[0, 0, 0],(172,447),help_)

        pygame.display.update()

