# -*- coding: utf-8 -*-

from Robot.Sensors.Simulated.Sensor import Sensor


class Magnetometer(Sensor):
    ###
    # This represents the Magnetometer Sensor class.
    # Magnetometer senses strong magnetic fields. Used to navigate and know where North is
    #
    # @param int heading - initial heading
    #
    ##
    def __init__(self, heading: int = 0):
        super(Magnetometer, self).__init__()
        self.heading = heading

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

    def getHeading(self) -> int:
        self._before()
        return self.heading

    ###
    # Updates the current heading of the robot.
    #
    # @param int heading
    #
    ##

    def updateHeading(self, heading: int):
        self.heading = heading
