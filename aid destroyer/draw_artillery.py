#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Juli
#
# Created:     25/12/2014
# Copyright:   (c) Juli 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import pygame
from pygame.locals import *
from colors import *


def draw_artillery(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT):

    # create objects tok be blitted
    artillery_rect = pygame.Rect(WINDOWWIDTH*0.4, WINDOWHEIGHT*0.8, \
    WINDOWWIDTH*0.6, WINDOWHEIGHT*0.2)

    # blit items
    pygame.draw.ellipse(DISPLAYSURF, GREY, artillery_rect, 0)