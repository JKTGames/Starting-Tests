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
import pygame
from pygame.locals import *

from draw_background import draw_background
from draw_ground import draw_ground
#from draw_civilians import draw_civilians
from draw_artillery import draw_artillery
#from draw_shots import draw_shots
#from draw_aid import draw_aid
#from draw_score_and_pause import draw_score_and_pause



def draw_screen(DISPLAYSURF):
    draw_background(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT)
    draw_ground(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT)
    #draw_civilians(DISPLAYSURF)
    draw_artillery(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT)
    #draw_shots(DISPLAYSURF)
    #draw_aid(DISPLAYSURF)
    #draw_score_and_pause(DISPLAYSURF)
