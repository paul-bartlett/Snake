#!/usr/bin/env python

#import everything
import pygame, random, time
from pygame.locals import *

#Global variables
display_width = 640
display_height = 640
FPS = 30
block_size = 10
score = 0;
white = (255,255,255)
black = (0,0,0)
orange = (255, 127, 80)
red = (255, 0, 0)

#Initialize pygame
pygame.init();

#Declaring the time lord
clock = pygame.time.Clock()

#Set the font
font = pygame.font.SysFont('Arial', 20);

#Set the screen size and name
screen = pygame.display.set_mode((display_width, display_height));
pygame.display.set_caption("Snake");

#Prints a message to the screen in the specified color
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [display_width/2, display_height/2])

#Draws a block on the screen of size block_size
def drawBlock(colour, x, y, block_size):
    pygame.draw.rect(screen, colour, [x, y, block_size, block_size]);

#Draws out the snake definded in snakeList
def snake(block_size, snakeList):
    for XnY in snakeList:
        drawBlock(orange, XnY[0], XnY[1], block_size)

#Begin main game loop
def gameLoop():

    #Defining LE snake dood
    head_x = display_width/2
    head_y = display_height/2
    head_x_change = 0
    head_y_change = 0
    exit = False
    gameOver = False
    snakeList = []
    snakeLength = 10

    #Generate random cordinates for the treat
    apple_x = random.randrange(0, (display_width-block_size)/10)*10 
    apple_y = random.randrange(0, (display_height-block_size)/10)*10

    #Gameloop starts
    while not exit:
        #When the game is lost
        while gameOver:
            screen.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red);
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:
                    gameOver = False
                    exit = True
                elif event.type == KEYDOWN:
                    if event.key == K_q:
                        exit = True
                        gameOver = False
                    elif event.key == K_c:
                        gameLoop()

        #When the game is running
        for event in pygame.event.get():
            if event.type == QUIT:
                exit = True
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    head_x_change = -block_size
                    head_y_change = 0
                elif event.key == K_RIGHT:
                    head_x_change = block_size
                    head_y_change = 0
                elif event.key == K_UP:
                    head_y_change = -block_size
                    head_x_change = 0
                elif event.key == K_DOWN:
                    head_y_change = block_size
                    head_x_change = 0

        #Check if snake has gone off the screen
        if head_x >= display_width or head_x <= 0 or head_y >= display_height or head_y <= 0:
            gameOver = True

        #Alter X and Y to change direction
        head_x += head_x_change
        head_y += head_y_change

        #Wipe your slate
        screen.fill(black)

        #Draw dat treat
        drawBlock(white, apple_x, apple_y, block_size)

        #Create a new block for the snake
        snakeHead = []

        #Add the X and Y cordinates for the new block
        snakeHead.append(head_x)
        snakeHead.append(head_y)

        #Add the new block to the snake body
        snakeList.append(snakeHead)

        #Check if the snake was suppose it increase in size
        if len(snakeList) > snakeLength:
            #If not, delete the last block of the snake (which creates the illusion that the snake is moving forward
            del snakeList[0]

        #Draws the snake
        snake(block_size, snakeList)

        #Updates the display
        pygame.display.update()

        #Check if good boy got the treat
        if head_x == apple_x and head_y == apple_y:
            apple_x = random.randrange(0, (display_width-block_size)/10)*10 
            apple_y = random.randrange(0, (display_height-block_size)/10)*10
            snakeLength += 1

        #locking in the FPS so my graphics card doesnt overheat
        clock.tick(FPS)

    pygame.quit();
    quit()

gameLoop()
