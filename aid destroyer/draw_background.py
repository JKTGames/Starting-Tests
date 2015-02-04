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
import os



def draw_background(DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT):

    cloud_x_size = WINDOWWIDTH * 0.2
    cloud_y_size = WINDOWHEIGHT * 0.16
    cloud_loc1 = (WINDOWWIDTH*0.34, WINDOWHEIGHT*0.15)
    cloud_loc2 = (WINDOWWIDTH*0.77, WINDOWHEIGHT*0.085)
    cloud_loc3 = (WINDOWWIDTH*(-0.08), WINDOWHEIGHT*0.1)

    # create objects to be blitted
    sky_rect = pygame.Rect(0, 0, WINDOWWIDTH, WINDOWHEIGHT)

    """ FIND A WAY TO BETTER REPRESENT FILENAME """
    print (os.path.expanduser("~\Documents\GitHub\Starting-Tests\\aid destroyer\\resources\cloud1.png"))
    # load images
    cloud = pygame.image.load(os.path.expanduser\
    ("~\Documents\GitHub\Starting-Tests\\aid destroyer\\resources\cloud1.png"))


    # scale images
    cloud = pygame.transform.scale(cloud, \
    (int(cloud_x_size), int(cloud_y_size)))



    # blit items
    pygame.draw.rect(DISPLAYSURF, LIGHTBLUE, sky_rect, 0)
    DISPLAYSURF.blit(cloud, cloud_loc1)
    DISPLAYSURF.blit(cloud, cloud_loc2)
    DISPLAYSURF.blit(cloud, cloud_loc3)


