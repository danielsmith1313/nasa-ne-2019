#File: ObstacleAvoidance.py
#Author: Daniel Smith
#Created: 9/12/18
#Description: Moves the robot forward in a straight line. Detects an obstacle in front of it and turns itself left and right to judge which way to turn
             #After turning, the robot continues in a straight line. Requires a distance sensor installed in a I2C slot

#The main controller for the robot

from RobotControl import RobotController
from di_sensors import easy_distance_sensor


class ObstacleAvoider:
    
    """
    Constructs the fields for the obstacle avoider object. Speed sets the speed of the motors and detectionRange sets the range at which the robot avoids an object
    The port for the robot must be I2C
    RobotController controls the movement and obstacle detection
    """
    def __init__(self, detectionRange):
        """Accepts detection range as a field, which is the length in inches before the robot attempts to redirect itself"""
        #Private fields
        #The length in inches before the robot redirects itself
        self.__detectionRange = detectionRange
        #Holds sensors
        self.__leftDistance = 0
        self.__rightDistance = 0
        self.__forwardDistance = 0
        #Robot Control object for movement and distance sensor
        self.__robotController = RobotController()
        
        
    
    def obstacleAvoidance(self):
        """(Run in a loop) detects when an obstacle is found"""
        
        
        
        #Get the distance each time from the distance sensor        
        self.__forwardDistance = self.__robotController.distanceSensor.getDistance()
        #Move forward
        self.__robotController.movementControl.setDirection("Forward")
        
            
        #If the reading is less then the set detection range for obstacles, stop the robot and run the avoidObstacle program
        if self.__forwardDistance <= self.__detectionRange:
            self.__robotController.movementControl.setDirection("Stop")
            self.avoidObstacle()
        #Otherwise continue forward
        else:
            pass
           
    
    def avoidObstacle(self):
        """Turns the robot to look left and right so that it can select the best way to go. It then turns that way."""
        #Get both left and right
        self.lookLeft90()
        self.lookRight180()
        #Compare the values
        if self.__leftDistance > self.__rightDistance:
            #Turn back around if the other side is the longer distance and resume the loop
            #Otherwise drive just continue the loop
            self.__robotController.deadReckoning.moveLeft(180)
            
            
    
    def lookLeft90(self):
        """Turns 90 degrees left and reads the input from the distance sensor"""
        #Uses encoded motors to tank turn 90 degrees
        self.__robotController.deadReckoning.moveLeft(90)
        #uses the RobotControl class to grab readings from the distance sensor
        self.__leftDistance = self.__robotController.distanceSensor.getDistance()
    
    def lookRight180(self):
        """Turns 180 degrees right and reads the input from the distance sensor"""
        #Uses encoded motors to tank turn 90 degrees
        self.__robotController.deadReckoning.moveRight(180)
        #uses the RobotControl class to grab readings from the distance sensor
        self.__rightDistance = self.__robotController.distanceSensor.getDistance()
        
    def stop(self):
        #Sets the robot to stop
        self.__robotController.movementControl.setDirection("Stop")