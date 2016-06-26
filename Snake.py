#!/usr/bin/env python

#import everything
import pygame, random
from pygame.locals import *

def dead(screen, score):
    font = pygame.font.SysFont('Arial', 20)
    post = font.render("Your score was: " + str(score), True, (255, 255, 255))
    screen.blit(t, (50, 300));
    pygame.display.update()
    pygame.time.wait(4000)

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 640))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    framerate = 10;
    direction = 0;
    score = 0
    
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    pygame.draw.rect(screen,(255, 255, 255), [20, 20, 20, 20])

    # screen.blit(background, (0, 0))

    while 1:
        clock.tick(framerate);
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_UP and direction != 0 : direction = 2
                elif event.key == K_DOWN and direction != 2 : direction = 0
                elif event.key == K_LEFT and direction != 1 : direction = 3
                elif event.key == K_RIGHT and direction != 3 : direction = 1 
                
        #
        # for o in objects:
        #     screen.blit(background, o.pos, o.pos)
        # for o in objects:
        #     o.move()
        #     screen.blit(o.image, o.pos)


if __name__ == '__main__': main()
