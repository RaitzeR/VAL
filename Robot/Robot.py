# -*- coding: utf-8 -*-
import math
from Helpers.Helpers import *
from gopigo import *

class Robot(object):
    ###
     # This represents the Robot object.
     # simX and simY are the positions where the robot thinks he is
     #
     # @param int size - Size of the robot (in cm)
     # @param int x - Initial x position of the robot
     # @param int y - Initial y position of the robot
     # @param int heading - Initial heading of the robot
     # @param int moverate - Initial moving rate of the rboot
     # @param int rotaterate - fixed max rotation rate of the robot
     # @param int acceleration - fixed acceleration rate of the robot
     # @param int rotationSpeed - fixed speed of the rotation
     # @param int maxSpeed - fixed max speed of the robot
     # @param int wheelDiameter - Diameter of the wheels on the robot
     #
     ##
    def __init__(self, size = 25, x = 0, y = 0, heading = 0, moverate = 0, rotaterate = 5, acceleration = 2, rotationSpeed = 5, maxSpeed = 15, wheelDiameter = 10):
        self.size = size
        self.x = x
        self.y = y
        self.simX = x
        self.simY = y
        self.xCenter = x + int(size / 2)
        self.yCenter = y + int(size / 2)
        self.simXCenter = x + int(size / 2)
        self.simYCenter = y + int(size / 2)
        self.heading = heading
        self.moverate = moverate
        self.rotaterate = rotaterate
        self.scannedPoints = []
        self.rotateLeft = False
        self.rotateRight = False
        self.rotate = False
        self.moveUp = False
        self.moveDown = False
        self.servoRight = False
        self.servoLeft = False
        self.acceleration = acceleration
        self.rotationSpeed = rotationSpeed
        self.maxSpeed = maxSpeed
        self.wheelDiameter = wheelDiameter
        self.servoPos = 0
        
    ###
     # This moves the robot based on where he thinks he is and is going.
     #
     ##
        
    def move(self):
        
        hallDistance = getCircumference(self.wheelDiameter) / self.magnetCount
        heading = self.magnetometer.getHeading()
        
        radians = math.radians(heading)
        x_speed = hallDistance * math.cos(radians)
        y_speed = hallDistance * math.sin(radians)
                
        self.setSimX(self.getSimX() + x_speed)
        self.setSimY(self.getSimY() + y_speed)
        
    ##
    #
    # Getter and setter methods
    #
    ##
        
    def getSize(self):
        return self.size

    
    def getSimX(self):
        return self.simX
    
    def setSimX(self,x):
        
        self.simX = x
        self.simXCenter = x + int(self.size / 2)
        
    def getSimY(self):
        return self.simY
    
    def setSimY(self,y):
        
        self.simY = y
        self.simYCenter = y + int(self.size / 2)
    
    def getX(self):
        return self.x
    
    def setX(self,x):
        
        self.x = x
        self.xCenter = x + int(self.size / 2)
        
    def getY(self):
        return self.y
    
    def setY(self,y):
        self.y = y
        self.yCenter = y + int(self.size / 2)
        
    def getHeading(self):
        return self.heading
    
    def getPosition(self):
        return (((self.getX() + (self.size / 2))),((self.getY() + (self.size / 2) )))
    
    def setHeading(self, heading):
        self.heading = heading
        
    def getMoverate(self):
        return self.moverate
    
    def setMoverate(self,moverate):
        self.moverate = moverate
        
    def addScannedPoint(self,point):
        self.scannedPoints.append(point)
        
    #####
    
    ###
    #
    # Sensor attachment methods. They accept the sensor object as a Parameter
    # and they set that sesor as active and add it to the robot object
    #
    ###
        
    def attachUltrasonic(self, ultrasonic):
        self.ultrasonic = ultrasonic
        ultrasonic.setActive()
        
    def attachHall(self, hall, magnetCount = 2):
        self.hall = hall
        hall.setActive()
        hall.addToRobot(self)
        self.magnetCount = magnetCount
        
    def attachMagnetometer(self,magnetometer):
        self.magnetometer = magnetometer
        magnetometer.setActive()
        
    def handleMovementCommands(self):
        #Move
        #Still have to do
        #TO DO
        #testing for the robot
        if self.moveUp:
            fwd()
        if self.moveDown:
            bwd()
        if self.rotateLeft:
            left()
        if self.rotateRight:
            right()
        if not self.moveUp and not self.moveDown and not self.rotateLeft and not self.rotateRight:
            stop()
        if self.servoLeft:
            enable_servo()
            servo(self.servoPos + 1)
        if self.servoRight:
            enable_servo()
            servo(self.servoPos - 1)
            
        if not self.servoLeft and not self.servoRight:
            disable_servo()
        return
    
    ###
     # This is called by the Hall sensor when it peaks. Then it moves our robot
     #
     ##
                
    def peaked(self):
        #The Hall sensor peaked.
        self.move()
        
    ###
     # This is the scan method. It asks the Environment if it hit anything, then it gets the distance
     #
     # @param \Environment\Environment - The environment object
     #
     ##
        
    def scan(self,ENVIRONMENT):
        degree = self.magnetometer.getHeading()
        distance = self.ultrasonic.scan(ENVIRONMENT,degree)
                
        if distance != False and distance < self.ultrasonic.scanLength:                    
            endpos = getEndPoint(degree,distance,self.getPosition())
            self.addScannedPoint(endpos)
                                    