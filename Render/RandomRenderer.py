#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:11:25 2017

@author: RaitzeR
"""
from Helpers.Helpers import getEndPoint
from Helpers.Colors import getColor

class RandomRenderer(object):
     ###
     # This represents the renderer for random things (Mainly the right panel).
     # 
     # @param \Environment\Environment - The Environment Class
     # @param \Render\Camera - The Camera Class
     # @param \Render\Display - The Display Class
     #
     ##
    def __init__(self, Environment, Camera, Robot, Display):
        self.display = Display
        self.camera = Camera
        self.environment = Environment
        self.robot = Robot
        
    def render(self):
        
        if self.environment.renderHallPeak:
            self.flashHall()
            self.environment.renderHallPeak = False
        
        panelRect = self.display.pygame.Rect(self.display.displayWidth - (self.display.displayWidth / 5),
                                    0,
                                    self.display.displayWidth / 5,
                                    self.display.displayHeight)
        self.display.pygame.draw.rect(self.display.displaySurface, getColor('silver'), panelRect)
        
        panelCenter = (self.display.displayWidth - (self.display.displayWidth / 5)) + ((self.display.displayWidth / 5) / 2)
        
        self.display.pygame.draw.circle(self.display.displaySurface, getColor('black'), (int(panelCenter),50), 20, 3)
        self.display.pygame.draw.line(self.display.displaySurface,getColor('black'),(int(panelCenter),70),(int(panelCenter),80),3)
        
        NarrowEndPoint1 = getEndPoint(self.robot.magnetometer.getHeading() - 0,
                                    5,
                                    (int(panelCenter), 180))
        
        NarrowEndPoint2 = getEndPoint(self.robot.magnetometer.getHeading() - 180,
                                    5,
                                    (int(panelCenter), 180))
        
        NarrowEndPoint3 = getEndPoint(self.robot.magnetometer.getHeading() - 90,
                                    40,
                                    (int(panelCenter), 180))
        
        SarrowEndPoint1 = getEndPoint(self.robot.magnetometer.getHeading() - 180,
                                    5,
                                    (int(panelCenter), 180))
        SarrowEndPoint2 = getEndPoint(self.robot.magnetometer.getHeading() - 0,
                                    5,
                                    (int(panelCenter), 180))
        SarrowEndPoint3 = getEndPoint(self.robot.magnetometer.getHeading() - 270,
                                    40,
                                    (int(panelCenter), 180))
        
        WarrowEndPoint1 = getEndPoint(self.robot.magnetometer.getHeading() - 90,
                                    5,
                                    (int(panelCenter), 180))
        WarrowEndPoint2 = getEndPoint(self.robot.magnetometer.getHeading() - 270,
                                    5,
                                    (int(panelCenter), 180))
        WarrowEndPoint3 = getEndPoint(self.robot.magnetometer.getHeading() - 180,
                                    40,
                                    (int(panelCenter), 180))
        
        EarrowEndPoint1 = getEndPoint(self.robot.magnetometer.getHeading() - 90,
                                    5,
                                    (int(panelCenter), 180))
        EarrowEndPoint2 = getEndPoint(self.robot.magnetometer.getHeading() - 270,
                                    5,
                                    (int(panelCenter), 180))
        EarrowEndPoint3 = getEndPoint(self.robot.magnetometer.getHeading() - 0,
                                    40,
                                    (int(panelCenter), 180))
        
        NEarrowEndPoint1 = getEndPoint(self.robot.magnetometer.getHeading() - 315,
                                    5,
                                    (int(panelCenter), 180))
        NEarrowEndPoint2 = getEndPoint(self.robot.magnetometer.getHeading() - 135,
                                    5,
                                    (int(panelCenter), 180))
        NEarrowEndPoint3 = getEndPoint(self.robot.magnetometer.getHeading() - 45,
                                    20,
                                    (int(panelCenter), 180))
        
        SEarrowEndPoint1 = getEndPoint(self.robot.magnetometer.getHeading() - 45,
                                    5,
                                    (int(panelCenter), 180))
        SEarrowEndPoint2 = getEndPoint(self.robot.magnetometer.getHeading() - 225,
                                    5,
                                    (int(panelCenter), 180))
        SEarrowEndPoint3 = getEndPoint(self.robot.magnetometer.getHeading() - 315,
                                    20,
                                    (int(panelCenter), 180))
        
        SWarrowEndPoint1 = getEndPoint(self.robot.magnetometer.getHeading() - 135,
                                    5,
                                    (int(panelCenter), 180))
        SWarrowEndPoint2 = getEndPoint(self.robot.magnetometer.getHeading() - 315,
                                    5,
                                    (int(panelCenter), 180))
        SWarrowEndPoint3 = getEndPoint(self.robot.magnetometer.getHeading() - 225,
                                    20,
                                    (int(panelCenter), 180))
        
        NWarrowEndPoint1 = getEndPoint(self.robot.magnetometer.getHeading() - 45,
                                    5,
                                    (int(panelCenter), 180))
        NWarrowEndPoint2 = getEndPoint(self.robot.magnetometer.getHeading() - 225,
                                    5,
                                    (int(panelCenter), 180))
        NWarrowEndPoint3 = getEndPoint(self.robot.magnetometer.getHeading() - 135,
                                    20,
                                    (int(panelCenter), 180))
        
        
        self.display.pygame.draw.circle(self.display.displaySurface, getColor('black'), (int(panelCenter),180), 35, 2)
        self.display.pygame.draw.circle(self.display.displaySurface, getColor('black'), (int(panelCenter),180), 30, 3)
        self.display.pygame.draw.polygon(self.display.displaySurface, getColor('black'), [WarrowEndPoint1, WarrowEndPoint2, WarrowEndPoint3], 2)
        self.display.pygame.draw.polygon(self.display.displaySurface, getColor('black'), [EarrowEndPoint1, EarrowEndPoint2, EarrowEndPoint3], 2)
        self.display.pygame.draw.polygon(self.display.displaySurface, getColor('red'), [NarrowEndPoint1, NarrowEndPoint2, NarrowEndPoint3], 2)
        self.display.pygame.draw.polygon(self.display.displaySurface, getColor('black'), [SarrowEndPoint1, SarrowEndPoint2, SarrowEndPoint3], 2)
        self.display.pygame.draw.polygon(self.display.displaySurface, getColor('black'), [NEarrowEndPoint1, NEarrowEndPoint2, NEarrowEndPoint3], 2)
        self.display.pygame.draw.polygon(self.display.displaySurface, getColor('black'), [SEarrowEndPoint1, SEarrowEndPoint2, SEarrowEndPoint3], 2)
        self.display.pygame.draw.polygon(self.display.displaySurface, getColor('black'), [SWarrowEndPoint1, SWarrowEndPoint2, SWarrowEndPoint3], 2)
        self.display.pygame.draw.polygon(self.display.displaySurface, getColor('black'), [NWarrowEndPoint1, NWarrowEndPoint2, NWarrowEndPoint3], 2)
        
        font = self.display.pygame.font.Font('freesansbold.ttf', 12)
        label = font.render("Distance Travelled:", 1, getColor('black'))
        self.display.displaySurface.blit(label, (int(panelCenter) - 90,270))
        
        label = font.render("%.2f" % (self.environment.totalMovement / 100) + " m", 1, getColor('black'))
        self.display.displaySurface.blit(label, (int(panelCenter) + 25,270))
        
        label = font.render("Points Scanned:", 1, getColor('black'))
        self.display.displaySurface.blit(label, (int(panelCenter) - 90,300))
        
        label = font.render(str(len(self.environment.robot.scannedPoints)), 1, getColor('black'))
        self.display.displaySurface.blit(label, (int(panelCenter) + 10,300))

    ###
     # Flashes the hall sensor on the right
     #
     ##
    
    def flashHall(self):
        panelCenter = (self.display.displayWidth - (self.display.displayWidth / 5)) + ((self.display.displayWidth / 5) / 2)
        self.display.pygame.draw.circle(self.display.displaySurface, getColor('red'), (int(panelCenter),50), 10, 5)
        self.display.pygame.draw.line(self.display.displaySurface,getColor('red'),(int(panelCenter) + 20,70),(getEndPoint(50, 15, (int(panelCenter) + 20,70))),3)
        self.display.pygame.draw.line(self.display.displaySurface,getColor('red'),(int(panelCenter) - 20,70),(getEndPoint(130, 15, (int(panelCenter) - 20,70))),3)
        self.display.pygame.draw.line(self.display.displaySurface,getColor('red'),(int(panelCenter) - 20,30),(getEndPoint(230, 15, (int(panelCenter) - 20,30))),3)
        self.display.pygame.draw.line(self.display.displaySurface,getColor('red'),(int(panelCenter) + 20,30),(getEndPoint(320, 15, (int(panelCenter) + 20,30))),3)

