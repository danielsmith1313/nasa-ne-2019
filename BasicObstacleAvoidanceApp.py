#File: BasicObstacleAvoidanceApp.py
#Author: Daniel Smith
#Created: 10/1/18
#Version: 1.0.0
#Description: Seperate window to control the obstacle avoidance of the robot

from tkinter import *

from RobotControl import RobotController
from ObstacleAvoidance import ObstacleAvoider

class BasicObstacleAvoidanceApplication(Frame):
    
    
    def __init__(self, master):
        
        #Declare constants
        DETECT_RANGE = 2
        #Import the constructor from the Frame class
        super(BasicObstacleAvoidanceApplication, self).__init__(master)
        
        #Root used to create a after loop
        self.__master = master
        #Code for creating a grid and widgets
        self.grid()
        self.createWidgets()
        
        #Define speed
        self.__speed = 200
        
        #RobotControl object to send input to the robot movement controller
        self.__obstacleAvoider = ObstacleAvoider(DETECT_RANGE)
        
        #Controls external loops
        self.__cancelID = None
        
    def createWidgets(self):
        """Initialization function that creates all widgets"""
        #Widgets that control how the robot is moving
        #Title label
        self.lblTitle = Label(self, text = "Runs the robot with obstacle avoidance")
        self.lblTitle.grid(row = 0, column = 0, columnspan = 5)
        #Button to start moving and avoiding obstacles
        self.btnObstacleAvoidance = Button(self, text = "Obstacle Avoidance", command = self.obstacleAvoidance)
        self.btnObstacleAvoidance.grid(row = 2, column = 0, sticky = NSEW)
        #Button to stop the robot
        self.btnStop = Button(self, text = "Stop", command = self.stop)
        self.btnStop.grid (row = 2, column = 1, sticky = NSEW)
        
    def obstacleAvoidance(self):
        self.__obstacleAvoider.obstacleAvoidance()
        self.__cancelID = self.__master.after(1, self.obstacleAvoidance)       
        
    def stop(self):
        self.master.after_cancel(self.__cancelID)
        self.__obstacleAvoider.stop()