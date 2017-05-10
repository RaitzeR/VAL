# -*- coding: utf-8 -*-

class Camera(object):
    ###
     # This represents the Camera class.
     # 
     # @param int slack - How far the robot has to move for the camera to follow
     #
     ##
    def __init__(self,slack):
        self.x = 0
        self.y = 0
        self.slack = 90
        
     ###
     # Adjust the camera based on the Display (the window) and the Robot we are tracking
     #
     # @param int - Width of the display
     # @param int - Height of the display
     #
     ##
        
    def adjustCamera(self, Display, Robot):
        if (self.x + (Display.displayWidth / 2)) - Robot.xCenter > self.slack:
            self.x = Robot.xCenter + self.slack - (Display.displayWidth / 2)
        elif Robot.xCenter - (self.x + (Display.displayWidth / 2)) > self.slack:
            self.x = Robot.xCenter - self.slack - (Display.displayWidth / 2)
        if (self.y + (Display.displayHeight / 2)) - Robot.yCenter > self.slack:
            self.y = Robot.yCenter + self.slack - (Display.displayHeight / 2)
        elif Robot.yCenter - (self.y + (Display.displayHeight / 2)) > self.slack:
            self.y = Robot.yCenter - self.slack - (Display.displayHeight / 2)
