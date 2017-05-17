# -*- coding: utf-8 -*-

import math
from Dependencies.XLoBorg import XLoBorg
from Robot.Sensors.Real.Sensor import Sensor

class Magnetometer(Sensor):
    ###
     # This represents the Magnetometer Sensor class.
     # Magnetometer senses strong magnetic fields. Used to navigate and know where North is
     #
     # @param int heading - initial heading
     #
     ##      
    def __init__(self):
        super(Magnetometer, self).__init__()
        XLoBorg.Init()
        self.updateHeading()
        
    ###
     # We use this to check if the Magnetometer sensor is active or not.
     #
     # @raise ValueError
     #
     ## 
        
    def _before(self):
        if not self.isActive:
            raise ValueError('Magnetometer Sensor is not Active')
            
    ###
     # Gets the current heading of the robot.
     #
     # @return heading
     #
     ##

    def getHeading(self):
        self._before()
        return self.heading
    
    ###
     # Updates the current heading of the robot.
     #
     # @param int heading
     #
     ##
        
    def updateHeading(self):
        x,y,z = XLoBorg.ReadCompassRaw()
        if y > 0:
            heading = 90 - math.atan2(x,y) * 180 / math.pi
        elif y < 0:
            heading = 270 - math.atan2(x,y) * 180 / math.pi
        elif y == 0 and x < 0:
            heading = 180
        else:
            heading = 0
        self.heading = heading