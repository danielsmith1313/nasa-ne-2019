#File: RobotControl.py
#Author: Daniel Smith
#Created: 9/5/18
#Version: 1.0.0
#Description: Gets input and controls the gopigo

#Import libraries

import logging
import time
try:
    import easygopigo3 as easy
except ImportError as e:
    logging.exception("Failed to import the easygopigo3 library")
except Exception as e:
    logging.exception("Something went wrong with the easygopigo3 library")
class RobotController:


    #Constructor
    def __init__(self, direction, speed):
        #Make sure the robot is setup successfully
        try:
            self.__direction = direction
            self.__speed = speed
            self.__gpg = easy.EasyGoPiGo3()
        except Exception as e:
            logging.exception("Something went wrong while setting up the robotcontroller object")
    def controlRobot(self):
        #setup the gopigo object
        #gpg = easy.EasyGoPiGo3()
        #set the starting speed of robot to __speed
        self.__gpg.set_speed(self.__speed)
        
        #Test if direction of user input, and set the motor to the correct setting
        #Robot could lose connection so we must use exception handling
        try:
            if (self.__direction == "Forward"):
                self.__gpg.forward()
            elif(self.__direction == "Backward"):
                self.__gpg.backward()
            elif(self.__direction == "Right"):
                self.__gpg.right()
            elif(self.__direction == "Left"):
                self.__gpg.left()
            elif(self.__direction == "Stop"):
                self.__gpg.stop()
        except Exception as e:
            logging.exception("Something went wrong when controlling the robot")
    
    
    #Setter for direction
    def setDirection(self,direction):
        #Data validation
        try:
            self.__direction = direction
        except Exception as e:
            logging.exception("Failed to set the direction of the robot")
    #Getter for direction
    def getDirection(self):
        return self.__direction
    
    #Setter for speed
    def setSpeed(self, speed):
        #Data validation
        try:
            self.__speed = speed
        except Exception as e:
            logging.exception("Failed to set the speed of the robot")
    
    def getSpeed(self):
        return self.__speed
    
    