#!/usr/bin/env python

#import everything
import pygame, random, time
from pygame.locals import *

#Global variables
displayWidth = 640
displayHeight = 640
FPS = 10
blockSize = 10
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
screen = pygame.display.set_mode((displayWidth, displayHeight));
pygame.display.set_caption("Snake");

#Prints a message to the screen in the specified color
def messageToScreen(text, color):
    #Create the surface with text and color
    textSurf = font.render(text, True, color)

    #Get the rectangle holding the text surface
    textRect = textSurf.get_rect()

    #Set that rectangle's center to the center of the page
    textRect.center = (displayWidth / 2), (displayHeight / 2)

    #Draw the text to the screen
    screen.blit(textSurf, textRect)

#Draws a block on the screen of size blockSize
def drawBlock(colour, x, y, blockSize):
    pygame.draw.rect(screen, colour, [x, y, blockSize, blockSize]);

#Draws out the snake definded in snakeList
def drawSnake(blockSize, snakeList):
    for XnY in snakeList:
        drawBlock(orange, XnY[0], XnY[1], blockSize)

#Begin main game loop
def gameLoop():

    #Defining LE snake dood
    headX = displayWidth/2
    headY = displayHeight/2
    headXChange = 0
    headYChange = 0
    exit = False
    gameOver = False
    snakeList = []
    snakeLength = 10

    #Generate random cordinates for the treat
    appleX = random.randrange(0, (displayWidth-blockSize)/10)*10 
    appleY = random.randrange(0, (displayHeight-blockSize)/10)*10

    #Gameloop starts
    while not exit:
        #When the game is lost
        while gameOver:
            screen.fill(white)
            messageToScreen("Game over, press C to play again or Q to quit", red);
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
                    headXChange = -blockSize
                    headYChange = 0
                elif event.key == K_RIGHT:
                    headXChange = blockSize
                    headYChange = 0
                elif event.key == K_UP:
                    headYChange = -blockSize
                    headXChange = 0
                elif event.key == K_DOWN:
                    headYChange = blockSize
                    headXChange = 0

        #Check if snake has gone off the screen
        if headX >= displayWidth or headX <= 0 or headY >= displayHeight or headY <= 0:
            gameOver = True

        #Alter X and Y to change direction
        headX += headXChange
        headY += headYChange

        #Wipe your slate
        screen.fill(black)

        #Draw dat treat
        drawBlock(white, appleX, appleY, blockSize)

        #Create a new block for the snake
        snakeHead = []

        #Add the X and Y cordinates for the new block
        snakeHead.append(headX)
        snakeHead.append(headY)

        #Add the new block to the snake body
        snakeList.append(snakeHead)

        #Check if the snake was suppose it increase in size
        if len(snakeList) > snakeLength:
            #If not, delete the last block of the snake (which creates the illusion that the snake is moving forward
            del snakeList[0]

        #Draws the snake
        drawSnake(blockSize, snakeList)

        #Updates the display
        pygame.display.update()

        #Check if good boy got the treat
        if headX == appleX and headY == appleY: 
            appleX = random.randrange(0, (displayWidth-blockSize)/10)*10 
            appleY = random.randrange(0, (displayHeight-blockSize)/10)*10
            snakeLength += 1

        #locking in the FPS so my graphics card doesnt overheat
        clock.tick(FPS)

    pygame.quit();
    quit()

gameLoop()
