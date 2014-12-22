#-------------------------------------------------------------------------------
# Name:        early_testing
# Purpose:
#
# Author:      Juli
#
# Created:     21/12/2014
# Copyright:   (c) Juli
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import pygame, sys
from pygame.locals import *

# Create the constants (go ahead and experiment with different values)
WINDOWWIDTH =  680
WINDOWHEIGHT = 720
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


def draw_walls(): # drawing and blitting in one function
    left_wall = pygame.Rect(0, 0, (WINDOWWIDTH * 0.2), WINDOWHEIGHT)
    right_wall = pygame.Rect((WINDOWWIDTH*0.8), 0,(WINDOWWIDTH * 0.2), \
    WINDOWHEIGHT)
    pygame.draw.rect(DISPLAYSURF, BROWN, left_wall, 0)
    pygame.draw.rect(DISPLAYSURF, BROWN, right_wall, 0)

def draw_player_char(current_player_location, current_player_color):
    player_char = pygame.Rect((current_player_location), (40, 40))
    pygame.draw.rect(DISPLAYSURF, current_player_color, player_char, 0)

def move_char():
    pass


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
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BGCOLOR

    # Initialize vars
    current_player_color = WHITE
    current_player_location = (WINDOWWIDTH * 0.2), (WINDOWHEIGHT* 0.75)

    print ('hi')
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Testing!')

    pygame.display.update()
    FPSCLOCK.tick(FPS)


    while True:

        checkForQuit()

        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEMOTION or event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos

            # idea for future testing
            """
            if player_is_jumping == True:
                current_player_color = RED
            else:
                current_player_color = WHITE
            """

        draw_walls()
        draw_player_char(current_player_location, current_player_color)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
