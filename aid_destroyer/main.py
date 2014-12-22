#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jk1214
#
# Created:     22/12/2014
# Copyright:   (c) jk1214 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame, sys
from pygame.locals import *

# Create the constants (go ahead and experiment with different values)
WINDOWWIDTH =  760
WINDOWHEIGHT = 620
FPS = 30

#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BLUE =    (  0,  0, 255)
DARKBLUE = (0, 0, 80)
PURPLE = (  160,  32,  240)
GREEN =         (  0, 255,   0)
DARKGREEN = (0, 150, 0)
ORANGE = (255,165,0)
DARKORANGE = (235, 145, 0)
DARKERORANGE = (205, 115, 0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREY = (190, 190, 190)
DARKGREY = (120, 120, 120)
BROWN = (153, 76, 0)
LIGHTGOLDENROD = (238, 221, 130)
LIGHTBLUE = (0, 191, 255)




def terminate():
    pygame.quit()
    sys.exit()

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

def main():
    global FPSCLOCK, DISPLAYSURF

    # Initialize vars


    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Testing!')

    # Set a new cursor
    pygame.mouse.set_cursor((8, 8), (4, 4), \
    (24, 24, 24, 231, 231, 24, 24, 24), (0, 0, 0, 0, 0, 0, 0, 0))

    while True:

        checkForQuit()

        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()

