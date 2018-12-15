## @file interface.py
#  @author Vaibhav Chadha
#  @brief implements the main interface of this game
#  @date 11/09/2018

x = 10
y = 40
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

import help_, highscore, theme
import pygame, sys
import GUI
from colors import *

## @brief Makes the main interface of this game
#  @details This will output the main page of this game by using the class above
def main():
  pygame.init()
  image1 = pygame.image.load("Images/Snake_Game_Logo_background.png")
  image2 = pygame.image.load("Images/Snake_image.png")

  #while loop required to always refresh the page
  run = True
  while run:
      game = pygame.display.set_mode((800, 610))
      game.blit(image1,(0,0))
      game.blit(image2,(550,0))
      mousepos = pygame.mouse.get_pos() #checking mouse position
      mouseclick = pygame.mouse.get_pressed()#checking mouse pressed
      pygame.display.set_caption("Lets Play")

      #Adding the play game button
      if (400 <= mousepos[0] <= 400+170 and 250 <= mousepos[1] <= 250+50 ):
        #checks if the mouse is hovering over the button
          GUI.button(game,darkgray, [400,250,170,50], 0)
          #checking if the button is clicked
          if mouseclick[0] == 1:
            theme.Themes.themes(100)        
      else:
          GUI.button(game,lightBlue, [400,250,170,50], 0)
      GUI.custom_text('Beginner',"Roboto-Light.ttf", 25, offwhite ,(438,260),game)

      if (430 <= mousepos[0] <= 430+220 and 350 <= mousepos[1] <= 350+50 ):
        #checks if the mouse is hovering over the button
          GUI.button(game,darkgray, [430,350,220,50], 0)
          #checking if the button is clicked
          if mouseclick[0] == 1:
            theme.Themes.themes(70)          
      else:
          GUI.button(game,lightBlue, [430,350,220,50], 0)
      GUI.custom_text('Intermediate',"Roboto-Light.ttf", 25, offwhite ,(470,357),game)

      if (400 <= mousepos[0] <= 400+180 and 450 <= mousepos[1] <= 450+50 ):
        #checks if the mouse is hovering over the button
          GUI.button(game,darkgray, [400,450,180,50], 0)
          #checking if the button is clicked
          if mouseclick[0] == 1:
            theme.Themes.themes(71)         
      else:
          GUI.button(game,lightBlue, [400,450,180,50], 0)
      GUI.custom_text('Advanced',"Roboto-Light.ttf", 25, offwhite ,(435,457),game)

      if (365 <= mousepos[0] <= 365+55 and 565 <= mousepos[1] <= 565+35 ):
          if mouseclick[0] == 1:
            help_.main()
      GUI.custom_text('Help',"Roboto-Light.ttf", 25, black ,(365,565),game)
      
      if (15 <= mousepos[0] <= 15+115 and 565 <= mousepos[1] <= 565+35 ):
        if mouseclick[0] == 1:
          highscore.main()

      if (725 <= mousepos[0] <= 725+50 and 565 <= mousepos[1] <= 565+35 ):
        if mouseclick[0] == 1:
          pygame.quit()
          sys.exit()
      
      pygame.display.update()

if __name__ == "__main__":
  main()



