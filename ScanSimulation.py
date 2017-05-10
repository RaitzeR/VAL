import random, sys, math, pygame

from pygame.locals import *
from Helpers.Helpers import *
from Helpers.IntersectingLineDetection import *
from Robot.Robot import Robot
from Robot.Sensors.Simulated.Ultrasonic import Ultrasonic
from Robot.Sensors.Simulated.Hall import Hall
from Robot.Sensors.Simulated.Magnetometer import Magnetometer

from Environment.Environment import Environment

from Helpers.Colors import getColor
from Handlers.EventHandler import TerminateHandler,RobotActionHandler

from Render.RobotViewRenderer import RobotViewRenderer
from Render.EnvironmentRenderer import EnvironmentRenderer
from Render.RandomRenderer import RandomRenderer
from Render.Camera import Camera
from Render.Display import Display

#1 pixel is 1cm

FPS = 30 #Frames per second to update the screen 
WINWIDTH = 1000 #Window width
WINHEIGHT = 480 #Window height
ROBOSIZE = 25 #Diameter of the robot in CM
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)
CAMERA_SLACK = 90

SCAN_ROTATION_SPEED = 100 #how many milliseconds does it take to turn 1 degree

FRICTION = 2


def main():
    global FPSCLOCK, DISPLAY
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAY = Display(WINWIDTH,WINHEIGHT)
    pygame.display.set_caption('ScanSimulator')
    while True:
        runSimulation()
        
def runSimulation():
    camera = Camera(CAMERA_SLACK)
    
    environment = Environment()
    environment.buildWalls()
    
    
    robot = Robot(ROBOSIZE,HALF_WINWIDTH,HALF_WINHEIGHT)
    
    ##Init Renderers
    
    environmentRenderer = EnvironmentRenderer(environment,camera,DISPLAY)
    randomRenderer = RandomRenderer(environment,camera,robot,DISPLAY)
    robotViewRenderer = RobotViewRenderer(robot,camera,DISPLAY)
    
    ##
    
    ##Add sensors to the robot
    
    ultrasonic = Ultrasonic(350)
    robot.attachUltrasonic(ultrasonic)
    hall = Hall()
    robot.attachHall(hall)
    magnetometer = Magnetometer()
    robot.attachMagnetometer(magnetometer)
    
    ##
    
    ##Add robot to the environment
    
    environment.addRobot(robot)
    
    ##
    
    while True:
        
        camera.adjustCamera(DISPLAY,robot)
        
        ## Render Stuff
        
        environmentRenderer.render(getColor('white'),getColor('white'),getColor('red'))
        randomRenderer.render()
        robotViewRenderer.render(getColor('blue'),getColor('white'),getColor('black'))
        
        ##
        
        ##Handle key presses
        
        for event in pygame.event.get():
            robot.moveDown,robot.moveUp,robot.rotateRight,robot.rotateLeft,robot.rotate,doScan = RobotActionHandler(event,robot)
            doTerminate = TerminateHandler(event)
            if doTerminate:
                terminate()
            if doScan:
                robot.scan(environment)
                
        ##
        
        ##handle robot movement

        robot.handleMovementCommands()                
        environment.triggerRobotRotation()        
        environment.triggerRobotMovement()
        
        ##
        
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def terminate():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
            
            
            
            
            
        