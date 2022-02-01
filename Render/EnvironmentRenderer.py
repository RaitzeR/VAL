#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:10:49 2017

@author: RaitzeR
"""

from Environment.Environment import Environment
from Render.Camera import Camera
from Render.Display import Display
from typing import Type, Tuple


class EnvironmentRenderer(object):
    ###
    # This represents the renderer for the Environment View.
    #
    # @param \Environment\Environment - The Environment class
    # @param \Render\Camera - The Camera class
    # @param \Render\Display - The Display class
    #
    ##
    def __init__(self, Environment: Type[Environment], Camera: Type[Camera], Display: Type[Display]):
        self.environment = Environment
        self.display = Display
        self.camera = Camera

    ###
    # Renders the environment to the view
    #
    # @param RGB (x,x,x) backgroundColor - RGB Value for the background
    # @param RGB (x,x,x) wallColor - RGB Value for the walls
    #
    ##

    def render(self, backgroundColor: Tuple[int, int, int], wallColor: Tuple[int, int, int],
               scanLineColor: Tuple[int, int, int]):
        self.fillBackground(backgroundColor)
        self.renderWalls(wallColor)
        for collisionPoint in self.environment.scanCollision:
            self.renderScanLines(collisionPoint[0], collisionPoint[1], scanLineColor)

        self.environment.scanCollision = []

    ###
    # Fills the background with color.
    #
    # @param RGB (x,x,x) color - RGB Value for the background
    #
    ##
    def fillBackground(self, color: Tuple[int, int, int]):
        self.display.displaySurface.fill(color)

    ###
    # Renders the walls.
    #
    # @param RGB (x,x,x) color - RGB Value for the background
    #
    ##
    def renderWalls(self, color: Tuple[int, int, int]):
        for wallLine in self.environment.walls:
            self.display.pygame.draw.line(self.display.displaySurface,
                                          color,
                                          (wallLine[0][0] - self.camera.x, wallLine[0][1] - self.camera.y),
                                          (wallLine[1][0] - self.camera.x, wallLine[1][1] - self.camera.y),
                                          1)

    ###
    # Renders the scan lines (from ultrasonic sensor).
    #
    # @param tuple roboPoint - Robot location
    # @param tuple intersectPoint- endpoint of the line
    # @param RGB (x,x,x) color - RGB Value for the lines
    #
    ##

    def renderScanLines(self, roboPoint: Tuple[int, int], intersectPoint: Tuple[int, int], color: Tuple[int, int, int]):
        self.display.pygame.draw.line(self.display.displaySurface,
                                      color,
                                      (roboPoint[0] - self.camera.x, roboPoint[1] - self.camera.y),
                                      (intersectPoint[0] - self.camera.x, intersectPoint[1] - self.camera.y),
                                      1)
