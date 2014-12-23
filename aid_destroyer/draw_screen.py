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

from main import WINDOWWIDTH, WINDOWHEIGHT
from colors import *
import pygame
from pygame.locals import *

# create objects to be blitted
ground = pygame.Rect(0, WINDOWHEIGHT * 0.9, WINDOWWIDTH, WINDOWHEIGHT * 0.1)

def draw_screen(DISPLAYSURF):
    pygame.draw.rect(DISPLAYSURF, BROWN, ground, 0)