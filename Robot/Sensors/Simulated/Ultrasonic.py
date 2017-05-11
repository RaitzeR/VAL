# -*- coding: utf-8 -*-

from Robot.Sensors.Simulated.Sensor import Sensor
from Helpers.IntersectingLineDetection import *
from Helpers.Helpers import *

class Ultrasonic(Sensor):
    ###
     # This represents the Ultrasonic sensor. It's used to measure distances
     # We use it to understand objects around us
     #
     # @param int scanLength - what's the maximum distance our scanner can scan
     #
     ##      
    def __init__(self, scanLength):
        super(Ultrasonic, self).__init__()
        self.scanLength = scanLength
        
    ###
     # We use this to check if the Ultrasonic sensor is active or not.
     #
     # @raise ValueError
     #
     ## 
    def _before(self):
        if not self.isActive:
            raise ValueError('Ultrasonic Sensor is not Active')
            
    ###
     # Do a scan. We ask the environment for a collision based on the angle and scanlength
     #
     # @param \Environment\Environment ENVIRONMENT - The current Environment object
     # @param int degree - The scan angle
     #
     # @return False / int distance - If the scan collides, it returns the distance, if not, returns false
     #
     ## 
    def scan(self, ENVIRONMENT,degree):
        self._before()
        return ENVIRONMENT.askForCollision(self.scanLength,degree)
        