#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 00:16:41 2017

@author: RaitzeR
"""

from Robot.Sensors.AbstractSensor import AbstractSensor

class Sensor(AbstractSensor):
    ###
     # This represents the parent class for all the Simulated Sensors.
     #
     ##  
    
    def __init__(self):
        super(Sensor, self).__init__()
        
    ###
     # We use this to check if the Sensor is active or not.
     #
     # @raise ValueError
     #
     ## 
    
    def _before(self):
        if not self.isActive:
            raise ValueError('Sensor is not Active')
    
    ###
     # Returns the state of the Sensor.
     #
     # @return State
     #
     ## 
        
    def showState(self):
        return self.state
    
    ###
     # Sets the state of the Sensor.
     #
     # @param state
     #
     ## 
        
    def setState(self,state):
        self.state = state