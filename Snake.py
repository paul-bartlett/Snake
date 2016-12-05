#!/usr/bin/env python

#import everything
import pygame, random
from pygame.locals import *

#This method is used to determine if the snake has licked the fruit yet...mmm
#def lick(x1, x2, y1, y2):
    
#Method handles all operations after the snake has hit a wall or itself
def rip(screen, score, font):
    post = font.render("Your score was: " + str(score), True, (255, 255, 255));
    screen.blit(post, (50, 300));
    pygame.display.update();
    pygame.time.wait(4000);
    pygame.quit();

#Contains initalization and main game loop
def main():

    #Local variables
    score = 0;
    white = (255,255,255)
    black = (0,0,0)

    #Defining LE snake dood
    head_x = 300
    head_y = 300
    head_x_change = 0

    #Initialize pygame
    pygame.init();

    #Declaring the time lord
    clock = pygame.time.Clock()

    #Set the font
    font = pygame.font.SysFont('Arial', 20);

    #Set the screen size and name
    screen = pygame.display.set_mode((640, 640));
    pygame.display.set_caption("Snake");

    #Begin main game loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit();
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    head_x_change = -10
                if event.key == K_RIGHT:
                    head_x_change = 10

            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    head_x_change = 0
                
        head_x += head_x_change

        #Wipe your slate
        screen.fill(black)

        #draw the head
        pygame.draw.rect(screen, white, [head_x, head_y, 20, 20]);
        pygame.display.update();

        #Keeping it at 15 FPS so my graphics card doesnt overheat
        clock.tick(15)

if __name__ == '__main__': main()
