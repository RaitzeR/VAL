import pygame, math, Helpers

from Helpers.Helpers import *
from Helpers.IntersectingLineDetection import *
from pygame.locals import *
from typing import Type, Tuple, Union
from Robot.Robot import Robot


class Environment(object):
    ###
    # This represents the Environment class. Environment handles the object physics for the Simulation.
    #
    ##
    def __init__(self):
        self.walls = []
        self.robotMovement = 0
        self.totalMovement = 0
        self.friction = 2
        self.scanCollision = []
        self.renderHallPeak = False

    ###
    # buildWalls is just a helper method to create the walls for the Environment
    #
    ##

    def buildWalls(self):
        l1p1 = (-100, -100)
        l1p2 = (1000, -100)
        l2p1 = (1000, -100)
        l2p2 = (1000, 1000)
        l3p1 = (1000, 1000)
        l3p2 = (-100, 1000)
        l4p1 = (-100, 1000)
        l4p2 = (-100, -100)

        self.walls = [(l1p1, l1p2), (l2p1, l2p2), (l3p1, l3p2), (l4p1, l4p2)]

    ###
    # add the robot into the environment object
    #
    # @param \Robot\Robot robot
    #
    ##

    def addRobot(self, robot: Type[Robot]):
        if not isinstance(robot, Robot):
            raise TypeError("Must be an instance of Robot class")
        self.robot = robot

    ###
    # Triggers the Robot Movement.
    #
    # TODO: This is ugly as hell, make it prettier
    #
    ##

    def triggerRobotMovement(self):
        if self.robot.moveUp:
            self.robot.moverate += self.robot.acceleration
        else:
            if self.robot.moverate > 0:
                self.robot.moverate -= self.friction
                if self.robot.moverate < 0:
                    self.robot.moverate = 0
        if self.robot.moveDown:
            self.robot.moverate -= self.robot.acceleration
        else:
            if self.robot.moverate < 0:
                self.robot.moverate += self.friction
                if self.robot.moverate > 0:
                    self.robot.moverate = 0

        if self.robot.moverate > 0:
            if self.robot.moverate > self.robot.maxSpeed:
                self.robot.moverate = self.robot.maxSpeed
        else:
            if abs(self.robot.moverate) > self.robot.maxSpeed:
                self.robot.moverate = -abs(self.robot.maxSpeed)

        speeds = self.moveRobot(self.robot.moverate)
        self.robotMovement += self.robot.moverate
        hallFrequency = getCircumference(self.robot.wheelDiameter) / self.robot.magnetCount

        if hallFrequency <= self.robotMovement:
            times = self.robotMovement / hallFrequency

            for time in range(math.floor(times)):
                self.robot.hall.peak()
                self.renderHallPeak = True

            self.totalMovement = self.totalMovement + self.robotMovement
            self.robotMovement = self.robotMovement - (hallFrequency * math.floor(times))

    ###
    # Moves the robot in the Environment, this is the robot's real position to move in
    #
    # @param int moverate - Moverate of the robot
    #
    # @return tuple - returns the x and y speeds
    #
    ##

    def moveRobot(self, moverate: int) -> Tuple[float, float]:
        heading = self.robot.magnetometer.getHeading()

        radians = math.radians(heading)
        x_speed = moverate * math.cos(radians)
        y_speed = moverate * math.sin(radians)

        self.robot.setX(self.robot.getX() + x_speed)
        self.robot.setY(self.robot.getY() + y_speed)

        return (x_speed, y_speed)

    ###
    # Triggers the robot Rotation. This updates the Magnetometer heading
    #
    ##

    def triggerRobotRotation(self):
        if self.robot.rotate:
            if self.robot.rotateLeft:
                self.robot.magnetometer.updateHeading(self.robot.magnetometer.getHeading() - self.robot.rotaterate)
            else:
                self.robot.magnetometer.updateHeading(self.robot.magnetometer.getHeading() + self.robot.rotaterate)

    ###
    # Gets the real position of the robot
    #
    # @return tuple - Returns the position
    ##

    def getRobotPosition(self) -> Tuple[int, int]:
        return (((self.robot.x + (self.robot.size / 2))), ((self.robot.y + (self.robot.size / 2))))

    ###
    # Asks the environment for collision between lines.
    #
    # @param int rayLength - Max length of the ultrasonic ray
    # @param int degrees - which direction the ultrasonic is sent to
    #
    # @return bool / int - Returns distance to the collision point, if there's no collision returns False
    #
    ##

    def askForCollision(self, rayLength: int, degrees: int) -> Union[bool, float]:
        endpos = getEndPoint(degrees, rayLength, self.getRobotPosition())

        for wallLine in self.walls:
            p3 = (wallLine[0][0], wallLine[0][1])
            p4 = (wallLine[1][0], wallLine[1][1])

            intersectPoint = calculateIntersectPoint(self.getRobotPosition(), endpos, p3, p4)

            if intersectPoint != None:
                self.collision(self.getRobotPosition(), intersectPoint)
                return getDistance(self.getRobotPosition(), intersectPoint)

        return False

    ###
    # Saves the collision data (for rendering purposes).
    #
    # @param tuple robotPosition - Position of the Robot
    # @param tuple endPosition - Position in which the collision happened
    #
    ##

    def collision(self, robotPosition: Tuple[int, int], endPosition: Tuple[int, int]):
        self.scanCollision.append((robotPosition, endPosition))
