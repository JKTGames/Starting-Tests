#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jk1214
#
# Created:     24/12/2014
# Copyright:   (c) jk1214 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
from colors import *


def draw_ground(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT):

    # create objects to be blitted
    flat_ground = pygame.Rect(0, WINDOWHEIGHT * 0.9, WINDOWWIDTH, \
    WINDOWHEIGHT * 0.1)

    # blit items
    pygame.draw.rect(DISPLAYSURF, BROWN, flat_ground, 0)