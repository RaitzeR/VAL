#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 23:20:51 2017

@author: RaitzeR
"""

import pygame
from pygame.locals import *

class Display(object):
    ###
     # Custom display class (so I don't have to pass around the display and pygame objects).
     #
     # @param int - Width of the display
     # @param int - Height of the display
     #
     ##
    
    def __init__(self,displayWidth,displayHeight):
        self.displayWidth = displayWidth
        self.displayHeight = displayHeight
        self.displaySurface = pygame.display.set_mode((displayWidth,displayHeight))
        self.pygame = pygame