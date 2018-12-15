## @file theme.py
#  @author Vaibhav Chadha
#  @brief implements the interface with theme options
#  @date 11/22/2018
from random import randint
from colors import *
import pygame, sys
import Gameplay
import init
import GUI

theme = 0

class Themes():

  ## @brief A function for running other files
  #  @details Executes another python file when this is selected, Given that the file is in same folder.
  #  @param runfilename The name of the file to be executed 
  def runfile(runfilename):
    with open(runfilename,"r") as rnf:
      exec(rnf.read())

  def themes(speed):
      pygame.init()
      run = True
      while run:
          theme = pygame.display.set_mode((500, 500))
          theme.fill(offwhite)
          mousepos = pygame.mouse.get_pos() #checking mouse position
          mouseclick = pygame.mouse.get_pressed()#checking mouse pressed
          pygame.display.set_caption("Snake 2.o")

          GUI.custom_text('Choose Your Theme',"Roboto-Light.ttf",45,[96,96,96],(70,50),theme)

          GUI.button(theme,lightBlue, [75,150,150,100], 0)
          GUI.custom_text('Regular',"Roboto-Light.ttf", 30,offwhite,(95,180),theme)        
          if (75 <= mousepos[0] <= 75+150 and 150 <= mousepos[1] <= 150+100 ):
              if mouseclick[0] == 1:
                  Gameplay.game(speed, lightB,lightR, white)

          GUI.button(theme,black1, [280,150,150,100], 0)
          GUI.custom_text('Dark',"Roboto-Light.ttf", 30,white,(325,180),theme)        
          if (280 <= mousepos[0] <= 280+150 and 150 <= mousepos[1] <= 150+100 ):
              if mouseclick[0] == 1:
                  Gameplay.game(speed,white,[255,255,0],black1)

          GUI.button(theme,[255,255,255], [175,300,160,100], 0)
          GUI.custom_text('Random',"Roboto-Light.ttf", 30,[0, 0, 0],(200,330),theme)        
          if (180 <= mousepos[0] <= 180+160 and 315 <= mousepos[1] <= 315+100 ):
              if mouseclick[0] == 1:
                x = randint(0, 1)
                if(x == 1): Gameplay.game(speed,lightB,lightR,white)
                else: Gameplay.game(speed,white,[255,255,0],black1)
        
          pygame.display.update()

