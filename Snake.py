#!/usr/bin/env python

#import everything
import pygame, random, time
from pygame.locals import *

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [display_width/2, display_height/2])

def drawBlock(colour, head_x, head_y, block_size):
    pygame.draw.rect(screen, colour, [head_x, head_y, block_size, block_size]);

def snake(block_size, snakeList):
    for XnY in snakeList:
        drawBlock(orange, [XnY[0]], [XnY[1]], block_size)


#Local variables
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

#Begin main game loop
def gameLoop():

    #Defining LE snake dood
    head_x = display_width/2
    head_y = display_height/2
    head_x_change = 0
    head_y_change = 0
    dead = False
    gameOver = False
    snakeList = []
    snakeHead = []

    apple_x = random.randrange(0, (display_width-block_size)/10)*10 
    apple_y = random.randrange(0, (display_height-block_size)/10)*10

    while not dead:
        while gameOver:
            screen.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red);
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        dead = True
                        gameOver = False
                    elif event.key == K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit();
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

        if head_x >= display_width or head_x <= 0 or head_y >= display_height or head_y <= 0:
            gameOver = True

        head_x += head_x_change
        head_y += head_y_change

        #Wipe your slate
        screen.fill(black)

        #Draw dat treat
        drawBlock(white, apple_x, apple_y, block_size)

        snakeHead.append(head_x)
        snakeHead.append(head_y)
        snakeList.append(snakeHead)
        
        snake(block_size, snakeList)

        #Check if good boy got the treat
        if head_x == apple_x and head_y == apple_y:
            apple_x = random.randrange(0, (display_width-block_size)/10)*10 
            apple_y = random.randrange(0, (display_height-block_size)/10)*10

        pygame.display.update();

        #locking in the FPS so my graphics card doesnt overheat
        clock.tick(FPS)

    pygame.quit();
    quit()

gameLoop()
