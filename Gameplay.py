## @file Gameplay.py
#  @author Andy Hameed | Usman Irfan
#  @brief implements gameplay and connects the different components of the game
#  @details including the snake, food item, score, exit and main interface
#  @date 11/09/2018

from random import randint
from Snake import *
from Food import *
from colors import *
import ScoreDisplay
import GUI

def game(speed, colour,food_colour, backgroundColour):
    pygame.event.clear()
    image = pygame.image.load("Images/barrier.png")

    #
    x = randint(0, grid_length) * size
    y = randint(0, grid_length) * size
    
    #defining a list to update snanke's length and
    #variable to increment snake's length, initially it would be 1
    snake_loc, snake_length = [], 1
    
    #Defining direction and axis as a binary digit using the mapping:
    #0 -> (- direction)             0 -> x-axis
    #1 -> (+ direction)             1 -> y-axis
    axis, score, direction = 0, 0, 1

    #Initializing food on the screen
    food_location = []
    food_x = randint(0, grid_length - 1) * size
    food_y = randint(0, grid_length - 1) * size
    food_location = [food_x, food_y]

    #Initialize snake and draw snake body on the screen
    snake = Snake(size, 0, 20, 1)
    pygame.draw.rect(win, colour , [x,y, size, size])
    food = Food(size)

    #Loop through the events as long as the game is running
    #still checks if snake is in initial position (static)
    run, still= True, True  
    while run:
        
        #time delay implements speed mechanism
        pygame.time.delay(speed) 

        #iterate through user events on keyboard and mouse
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            #Detect key presses and change axis and direction accordingly
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT):
                    if (snake.axis or still): snake.direct = -1; still = False
                    snake.axis = 0
                if (event.key == pygame.K_RIGHT):
                    if (snake.axis or still): snake.direct = 1; still = False 
                    snake.axis = 0
                if (event.key == pygame.K_UP):
                    if (not snake.axis or still): snake.direct = -1; still = False 
                    snake.axis = 1
                if (event.key == pygame.K_DOWN):
                    if (not snake.axis or still): snake.direct = 1; still = False 
                    snake.axis = 1


        #Snake changes movement depending on axis and direction
        if (snake.axis):
            y += (size)*snake.direct
        else:
            x += (size)*snake.direct
        
        boundary_condition = (x < 0 or y < 0 or y > screenSize - size or x > screenSize - size)
        maze_x = x == 100
        maze_y = abs(y - 210) <= 110

        maze2_x = x == 380
        
        if  (speed == 100):
            if x < 0:
                x = screenSize - size
            if y < 0:
                y = screenSize - size
            if y > screenSize - size:
                y = 0
            if x > screenSize - size:
                x = 0

        elif (speed == 70):
            #Boundary conditions for snake hitting window edge
            if (boundary_condition):
                run = False
                ScoreDisplay.display(score,speed, colour,food_colour, backgroundColour)
                
        elif (speed == 71):
            if ((maze_x and maze_y) or boundary_condition or (maze2_x and maze_y)):
                run = False
                ScoreDisplay.display(score,speed, colour,food_colour, backgroundColour)         

        #detect collision between food and snake head
        if(abs(x - food_location[0]) < 15 and abs(y - food_location[1]) < 15):
            if (speed == 100):
                score += 5
            elif (speed == 70):
                score += 7
            else:
                score += 10

            #increment the length by 3 unit every time
            snake_length += 3

            
        win.fill(backgroundColour)
        if speed == 71:
            win.blit(image,(100,100))
            win.blit(image,(380,100))

        #Display Score
        sc_color = black if backgroundColour[0] == 255 else white
        GUI.custom_text(" " + str(score),"Roboto-Light.ttf",30,sc_color,(0,0),win)
        
        if ([x,y] in snake_loc) and snake_length > 1:        
           ScoreDisplay.display(score,speed, colour,food_colour, backgroundColour)
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)

        snake_loc.append(snake_head)
        
        #consumption of food block
        food.redraw_food(x, y, food_location, screenSize, snake_loc)

        snake_blocks = len(snake_loc)

        #Draw food item
        food.draw_food(food_colour, food_location)

        #update snake blocks based on changes in coordinates
        if snake_blocks > snake_length:
            del snake_loc[0]
        '''
        Logic for updating the length is taken from:
        CodeWithHarry, CodeWithHarry. “Snakes Game: Length Increment Logic - Python Game Development Using Pygame In Hindi #17.”
        YouTube, YouTube, 2 Oct. 2018,
        www.youtube.com/watch?v=mkGJb0W03DM&index=17&list=PLu0W_9lII9ailUQcxEPZrWgDoL36BtPYb.
        '''
        
        #Draw snake
        snake.draw(colour,snake_loc)

        #update display
        pygame.display.update()

    pygame.quit()
