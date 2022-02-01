# -*- coding: utf-8 -*-

from Robot.Sensors.Simulated.Sensor import Sensor
from Robot.Robot import Robot
from typing import Type


class Hall(Sensor):
    ###
    # This represents the Hall Sensor class.
    # Hall sensor senses when a magnet is close to it. It can be used how many times a tire
    # has revolved around itself
    #
    ##
    def __init__(self):
        super(Hall, self).__init__()

    ###
    # We use this to check if the Hall sensor is active or not.
    #
    # @raise ValueError
    #
    ##

    def _before(self):
        if not self.isActive:
            raise ValueError('Hall Sensor is not Active')

    ###
    # Adds the sensor to the robot and saves the robot object to the sensor.
    #
    # @param \Robot\Robot robot - Robot object
    #
    ##

    def addToRobot(self, robot: Type[Robot]):
        self._before()
        self.robot = robot

    ###
    # Tells the robot that is has peaked (there is a magnet near it).
    #
    ##

    def peak(self):
        self._before()
        # print("Peaked")
        self.robot.peaked()
