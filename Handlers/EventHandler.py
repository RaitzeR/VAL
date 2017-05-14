# -*- coding: utf-8 -*-
import pygame

from pygame.locals import *

###
 # Handles the terminate keypress
 # 
 # @param \pygame\event event - pygame keypress event
 #
 # @return bool - whether or not  to terminate the program
 ##

def TerminateHandler(event):
    Terminate = False
    if event.type == QUIT:
        Terminate = True
    elif event.type == KEYUP:
        if event.key == K_ESCAPE:
            Terminate = True
            
    return Terminate

###
 # Handles the keypresses for robot actions
 # 
 # @param \pygame\event event - pygame keypress event
 # @param \Robot\Robot - The Robot Class
 #
 # @return bool,bool,bool,bool,bool,bool - Bool values for the robot movements
 ##

def RobotActionHandler(event,robot):
    
    Scan = False
    moveDown = robot.moveDown
    moveUp = robot.moveUp
    rotateRight = robot.rotateRight
    rotateLeft = robot.rotateLeft
    rotate = robot.rotate
    servoLeft = robot.servoLeft
    servoRight = robot.servoRight
    
    if event.type == KEYDOWN:
        if event.key in (K_UP, K_w):
            moveDown = False
            moveUp = True
        if event.key in (K_DOWN, K_s):
            moveDown = True
            moveUp = False
        if event.key in (K_LEFT, K_a):
            rotateRight = False
            rotateLeft = True
            rotate = True
        if event.key in (K_RIGHT, K_d):
            rotateRight = True
            rotateLeft = False
            rotate = True
        if event.key == K_x:
            Scan = True
        if event.key == K_q:
            servoLeft = True
            servoRight = False
        if event.key == K_e:
            servoRight = True
            servoLeft = False
    if event.type == KEYUP:
        if event.key in (K_UP, K_w):
            moveUp = False
        if event.key in (K_DOWN, K_s):
            moveDown = False
        if event.key in (K_LEFT, K_a):
            rotaterate = 0
            rotateLeft = False
            rotate = False
        if event.key in (K_RIGHT, K_d):
            rotaterate = 0
            rotateRight = False
            rotate = False
        if event.key == K_q:
            servoLeft = False
        if event.key == K_e:
            servoRight = False
            
    return moveDown,moveUp,rotateRight,rotateLeft,rotate,Scan,servoLeft,servoRight