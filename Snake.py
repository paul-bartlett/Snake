#!/usr/bin/env python

#import everything
import pygame, random, time
from pygame.locals import *

def message_to_screen(screen, display_width, display_height, font, msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [display_width/2, display_height/2])

#Contains initalization and main game loop
def main():

    #Local variables
    display_width = 640
    display_height = 640
    FPS = 30
    block_size = 20
    score = 0;
    white = (255,255,255)
    black = (0,0,0)
    red = (255, 0, 0)

    #Defining LE snake dood
    head_x = display_width/2
    head_y = display_height/2
    head_x_change = 0
    head_y_change = 0

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
    while True:

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
            message_to_screen(screen, display_width, display_height, font, "You Lose!", red)
            pygame.display.update()
            time.sleep(2)
            pygame.quit();

        head_x += head_x_change
        head_y += head_y_change

        #Wipe your slate
        screen.fill(black)

        #draw the head
        pygame.draw.rect(screen, white, [head_x, head_y, block_size, block_size]);
        pygame.display.update();

        #locking in the FPS so my graphics card doesnt overheat
        clock.tick(FPS)

if __name__ == '__main__': main()

