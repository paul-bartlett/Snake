#!/usr/bin/env python

#import everything
import pygame, random
from pygame.locals import *

#This method is used to determine if the snake has licked the fruit yet...mmm
def lick(x1, x2, y1, y2):
    
#Method handles all operations after the snake has hit a wall or itself
def rip(screen, score, font):
    post = font.render("Your score was: " + str(score), True, (255, 255, 255));
    screen.blit(post, (50, 300));
    pygame.display.update();
    pygame.time.wait(4000);
    pygame.quit();

#Contains initalization and main game loop
def main():

    #local variables
    clock = pygame.time.Clock();
    framerate = 10;
    direction = 0;
    score = 0;
    font = pygame.font.SysFont('Arial', 20);

    #initialize pygame
    pygame.init();
    
    #Set the screen size
    screen = pygame.display.set_mode((640, 640));
    
    #Initialize the background
    background = pygame.Surface(screen.get_size());
    background = background.convert();
    background.fill((250, 250, 250));


    pygame.display.set_caption("Snake");
    pygame.draw.rect(screen,(255, 255, 255), [20, 20, 20, 20]);

    #Begin main game loop
    while True:

        #Continue refreshing the snake at the current framerate value
        clock.tick(framerate);

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit();
                
            #If a key is pressed detect which direction it was in and dont allow 180 noscopes
            elif event.type == KEYDOWN:
                if event.key == K_UP and direction != 0 : direction = 2
                elif event.key == K_DOWN and direction != 2 : direction = 0
                elif event.key == K_LEFT and direction != 1 : direction = 3
                elif event.key == K_RIGHT and direction != 3 : direction = 1 
        
        #Update the score on the screen
        post = font.render(str(score), True, (0, 0, 0));
        screen.blit(post, 10, 10);

        pygame.display.update();

if __name__ == '__main__': main()
