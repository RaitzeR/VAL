#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:10:55 2017

@author: RaitzeR
"""
from Helpers.Helpers import getEndPoint
from Render.Camera import Camera
from Render.Display import Display
from typing import Type, Tuple
from Robot.Robot import Robot


class RobotViewRenderer(object):
    ###
    # This represents the renderer for the robot view.
    #
    # @param \Robot\Robot - The Robot class
    # @param int - Width of the display
    # @param int - Height of the display
    # @param \Render\Display - The Display Class
    #
    ##
    def __init__(self, Camera: Type[Camera], Display: Type[Display], Robot: Type[Robot]):
        self.display = Display
        self.robot = Robot
        self.camera = Camera

    ###
    # Renders the robot view
    #
    # @param RGB (x,x,x) robotColor - RGB Value for the robot
    # @param RGB (x,x,x) robotScannerPointColor - RGB Value for the scanned points
    #
    ##

    def render(self, robotColor: Tuple[int, int, int], robotArrowColor: Tuple[int, int, int],
               robotScannedPointColor: Tuple[int, int, int], renderBotView: bool = False,
               botViewColor: Tuple[int, int, int] = (255, 0, 0)):
        self.renderRobot(robotColor, robotArrowColor, botViewColor)
        self.renderRobotPoints(robotScannedPointColor)
        if renderBotView:
            self.renderGhostRobot(botViewColor)

    ###
    # Renders the robot
    #
    # @param RGB (x,x,x) robotColor - RGB Value for the robot body
    # @param RGB (x,x,x) robotScannerPointColor - RGB Value for the directional arrow
    #
    ##

    def renderRobot(self, robotColor: Tuple[int, int, int], robotArrowColor: Tuple[int, int, int], botViewColor: Tuple[int, int, int]):
        self.renderRobotBody(robotColor, botViewColor)
        self.renderRobotArrow(robotArrowColor)

    ###
    # Renders the robot body
    #
    # @param RGB (x,x,x) color - RGB Value for the robot body
    #
    ##
    def renderRobotBody(self, color: Tuple[int, int, int]):
        roboRectangle = self.display.pygame.Rect(
            (self.robot.x - self.camera.x,
             self.robot.y - self.camera.y,
             self.robot.size,
             self.robot.size)
        )
        self.display.pygame.draw.rect(self.display.displaySurface, color, roboRectangle)

    def renderGhostRobot(self, color: Tuple[int, int, int]):
        roboRectangle = self.display.pygame.Rect(
            (self.robot.simX - self.camera.x,
             self.robot.simY - self.camera.y,
             self.robot.size,
             self.robot.size)
        )
        self.display.pygame.draw.rect(self.display.displaySurface, color, roboRectangle)

    ###
    # Renders the robots directional arrow
    #
    # @param RGB (x,x,x) color - RGB Value for the arrow
    #
    ##
    def renderRobotArrow(self, color: Tuple[int, int, int]):
        roboPoint = (
            (self.robot.x + (self.robot.size / 2)) - self.camera.x,
            (self.robot.y + (self.robot.size / 2)) - self.camera.y)
        arrowEndPoint = getEndPoint(self.robot.magnetometer.getHeading(),
                                    self.robot.size,
                                    roboPoint)
        self.display.pygame.draw.line(self.display.displaySurface,
                                      color,
                                      roboPoint,
                                      arrowEndPoint,
                                      1)

    ###
    # Renders the robots scanned points
    #
    # @param RGB (x,x,x) color - RGB Value for the scanned points
    #
    ##
    def renderRobotPoints(self, color: Tuple[int, int, int]):
        for scannedPoint in self.robot.scannedPoints:
            pointRect = self.display.pygame.Rect(scannedPoint[0] - self.camera.x,
                                                 scannedPoint[1] - self.camera.y,
                                                 1,
                                                 1)
            self.display.pygame.draw.rect(self.display.displaySurface, color, pointRect)
