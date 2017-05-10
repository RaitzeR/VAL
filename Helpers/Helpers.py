# -*- coding: utf-8 -*-

import math

###
 # Gets the end point of a line based on angle, length of the line and starting position
 #
 # @param int angle - Angle of the line
 # @param int length - Length of the line
 # @param tuple pos - starting position of the line
 #
 # @return tuple - The end point
 #
 ##

def getEndPoint(angle, length, pos):
        radians = math.radians(angle)
        
        x = pos[0] + length * math.cos(radians)
        y = pos[1] + length * math.sin(radians)
        
        return (x,y)
    
###
 # Adjust a point to the camera
 #
 # @param tuple intersectPoint - the Point to which to adjust
 # @param /Render/Camera camera - The camera object
 #
 # @return tuple - The adjusted point
 #
 ##

def adjustIntersect(intersectPoint,camera):
    x = intersectPoint[0] + camera.x
    y = intersectPoint[1] + camera.y
                      
    return (x,y)

###
 # Get distance between two points
 #
 # @param tuple point1 - First point
 # @param tuple point2 - Second point
 #
 # @return - The distance
 #
 ##

def getDistance(point1,point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

###
 # Get circumference based on diameter
 #
 # @param int diameter - The diameter
 #
 # @return float - The diameter
 #
 ##

def getCircumference(diameter):
    return 2*math.pi*(diameter / 2)