#File: ManualControlApp.py
#Author: Daniel Smith
#Created: 10/1/18
#Version: 1.0.0
#Description: Seperate window to control the gopigo basic movements

from tkinter import *
from RobotControl import RobotController

class ManualControlApplication(Frame):
    """Basic window frame template for manual control"""
    

    def __init__(self, master):
        
        #Define constants
        self.CONTROL_BUTTON_HEIGHT = 5
        self.CONTROL_BUTTON_WIDTH = 10
        
        #Import the constructor from the Frame class
        super(ManualControlApplication, self).__init__(master)
        
        #Code for creating a grid and widgets
        self.grid()
        self.createWidgets()
        
        #Define speed
        self.__speed = 200
        
        #RobotControl object to send input to the robot movement controller
        
        self.__robotController = RobotController()
        
        

    def createWidgets(self):
        
        #Widgets that control how the robot is moving
        #Title label
        self.lblTitle = Label(self, text = "Controls robot movement")
        self.lblTitle.grid(row = 0, column = 0, columnspan = 5)
        #Speed entry
        self.entrySpeed = Entry(self)
        self.entrySpeed.grid(row = 5, column = 0, columnspan = 5)
        #Buttons
        self.btnForward = Button(self, text = "Forward", command = self.forward, height = self.CONTROL_BUTTON_HEIGHT, width = self.CONTROL_BUTTON_WIDTH)
        self.btnForward.grid(row = 1, column = 1, sticky = NSEW)
        self.btnBackward = Button(self, text = "Backward", command = self.backward, height = self.CONTROL_BUTTON_HEIGHT, width = self.CONTROL_BUTTON_WIDTH)
        self.btnBackward.grid(row = 3, column = 1, sticky = NSEW)
        self.btnRight = Button(self, text = "Right", command = self.right, height = self.CONTROL_BUTTON_HEIGHT, width = self.CONTROL_BUTTON_WIDTH)
        self.btnRight.grid(row = 2, column = 2, sticky = NSEW)
        self.btnLeft = Button(self, text = "Left", command = self.left, height = self.CONTROL_BUTTON_HEIGHT, width = self.CONTROL_BUTTON_WIDTH)
        self.btnLeft.grid(row = 2, column = 0, sticky = NSEW)
        self.btnStop = Button(self, text = "Stop", command = self.stop, height = self.CONTROL_BUTTON_HEIGHT, width = self.CONTROL_BUTTON_WIDTH)
        self.btnStop.grid(row = 4, column = 1, sticky = NSEW)
        #Set speed button
        self.btnSetSpeed = Button(self, text = "Set Speed", command = self.setSpeed)
        self.btnSetSpeed.grid(row = 6, column = 1, sticky = NSEW)
        
        #configure the columns and rows to autosize
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)
        self.rowconfigure(4, weight = 1)
        
        
    #Handles the five buttons to control the robot
    def forward(self):
        """Event handler for the forward button, drives the robot forward endlessly"""
        self.__robotController.movementControl.setDirection("Forward")
    
    def backward(self):
        """Event handler for the backward button, drives the robot backwards endlessly"""
        self.__robotController.movementControl.setDirection("Backward")
        
    def right(self):
        """Event handler for the right button, drives the robot to the right endlessly"""
        self.__robotController.movementControl.setDirection("Right")
        
    def left(self):
        """Event handler for the left button, drives the robot to the left endlessly"""
        self.__robotController.movementControl.setDirection("Left")
        
    def stop(self):
        """Event handler for the stop button, stops the robot"""
        self.__robotController.movementControl.setDirection("Stop")
    
    def setSpeed(self):
        """Event handler that lets the speed of the robot from the entrySpeed widget"""
        
        
        #Get the user input from the entry widget
        try:
            self.__speed = self.MovementControl.getSpeed()
        except Exception as e:
            logging.exception("Something went wrong while gettin the speed input from the user")
        
        #Set the speed and update the motors on the robot
        self.__robotController.MovementControl.setSpeed(self.__speed)