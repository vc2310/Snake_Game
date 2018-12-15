## @file highscore.py
#  @author Vaibhav Chadha
#  @brief implements the highscore interface
#  @date 11/09/2018
import pygame, sys, Interface, pathlib
import GUI
from colors import *

## @brief A Class that will contain useful functions in order for the creation of highscore page
class HighScore():

  ## @brief Finds the highest score from the file
  #  @details This writes the input from the file in an array and find the max number from it
  def findHighScore():
    file = pathlib.Path("highscore.txt")
    if file.exists ():
      infile = open("highscore.txt","r")
      mylist = []
      for line in infile:
        a = line.strip()
        mylist.append(a)
      if (len(mylist) == 0):
        return 0
      else: return max(mylist)
    else:
      makingfile = open("highscore.txt","w+")
      return 0
## @brief Makes the highscore interface
#  @details This will output the final interface using the class above
#           which can be seen by executing this function.
def main():
    pygame.init()
    while True:
      mousepos = pygame.mouse.get_pos() #checking mouse position
      mouseclick = pygame.mouse.get_pressed()#checking mouse pressed
      highscore = pygame.display.set_mode((300, 150))
      highscore.fill(white)
      pygame.display.set_caption("Highscore")

      GUI.custom_text('Highest Score: ' + str(HighScore.findHighScore()),"Roboto-Light.ttf", 30,black,(10,20),highscore)

      GUI.custom_text('Main Menu',"Roboto-Light.ttf", 25,black,(90,70),highscore)
      if (90 <= mousepos[0] <= 90+120 and 70 <= mousepos[1] <= 70+27 ):
          if mouseclick[0] == 1:
            Interface.main()            

      GUI.custom_text('Quit',"Roboto-Light.ttf", 25,black,(125,105),highscore)
      if (125 <= mousepos[0] <= 125+45 and 105 <= mousepos[1] <= 105+27 ):
            if mouseclick[0] == 1:
              pygame.quit()
              sys.exit()
              
      pygame.display.update()
