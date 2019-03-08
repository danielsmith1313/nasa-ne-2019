#Filename: Application.py
#Author: Daniel Smith
#Created: 9/5/18
#Version 1.2.0
#Description: Creates a custom frame by using the tkinter Frame class

#-- TODO: Seperate each file window into a new file --
#import gui library
from tkinter import *

#Import libraries
#Allows control of the robot
from RobotControl import RobotController
#Controls autonomous movement with avoidance
from ObstacleAvoidance import ObstacleAvoider
#Allows manual control and stopping of applications
from ManualControlApp import ManualControlApplication
#The application window for the basic obstacle avoidance window
from BasicObstacleAvoidanceApp import BasicObstacleAvoidanceApplication
#Class that finds the shortest path
from Dijkstra import Dijkstras
#Converts a normal input to be able to be read by Dijkstra's algorithm
from NodeMapper import map
#Library that is used to create a scatter plot showing the nodes
import matplotlib.pyplot as plt

#json, JavaScript Object Notation allows easier reading and writing of files
import json

#Exception handling
import logging

#----------
#Main application
#----------
#Child of the frame class which is used to build a gui frame
class Application(Frame):
    #Class description
    """This application builds the main application window in which other windows are opened to control the robot"""


    #Constructor
    def __init__(self, master):
        #Import the constructor from the Frame class
        super(Application, self).__init__(master)
        
        #positioning used to place widgets
        self.grid()
        #Run the function to setup the widgets on the screen
        self.createWidgets()
        


    #Creates widgets on the window frame
    def createWidgets(self):

        ###Create Labels###

        #Creates a label object
        self.lblTitle = Label(self, text="GoPiGo Control Window")
        #Applies the grid to the object allowing it to be positioned
        self.lblTitle.grid(row = 0,column = 0,sticky = W)

        ###Create Buttons###
        self.btnManualControl = Button(self, text = "Manual Control", command = self.manualControl)
        self.btnManualControl.grid(row = 1, column = 0, sticky = NSEW)
        self.btnBasicObstacleAvoidance = Button(self, text = "Basic Obstacle Avoidance", command = self.basicObstacleAvoidance)
        self.btnBasicObstacleAvoidance.grid(row = 2, column = 0, sticky = NSEW)
        self.btnNodeBasedPathfinding = Button(self, text = "Node Based Pathfinding", command = self.nodeBasedPathfinding)
        self.btnNodeBasedPathfinding.grid(row = 3, column = 0, sticky = NSEW)
        
    def manualControl(self):
        """Event handler for btnManualControl. Allows the user to manually control the GoPiGo"""
        
        #Creates a new empty window on top of the current one
        self.manualControlWindow = Toplevel(self.master)
        
        #Sets the dimensions of the window
        self.manualControlWindow.geometry("800x600")
        #Applies the ManualControlApplication framework to the window
        #Note: self.manualControlApp is the object for the ManualControlApplication class
        self.manualControlApp = ManualControlApplication(self.manualControlWindow)
        #Handles the closing of the window, ending the program
        self.manualControlWindow.protocol("WM_DELETE_WINDOW",self.manualControlCloseApplication)
        
    def manualControlCloseApplication(self):
        """Event handler for the closing of the ManualControlApplication"""
        #Stop the main application
        self.manualControlApp.stop()
        try:
            #Try closing the window
            self.manualControlWindow.destroy()
        except Exception as e:
            logging.exception("Something went wrong while trying to close the window")

    def nodeBasedPathfinding(self):
        """Event handler for btnNodeBasedPathfinding"""
        #Creates a new empty window
        self.nodeBasedPathfindingWindow = Toplevel(self.master)
        #Sets the dimensions of the window
        self.nodeBasedPathfindingWindow.geometry("300x300")
        #Applies the framework for the new window by putting the window created into the nodeBasedPathfinding class
        self.nodeBasedPathfindingApp = NodeBasedPathfinding(self.nodeBasedPathfindingWindow)
    def basicObstacleAvoidance(self):
        
        """Event handler for btnBasicObstacleAvoidance. Sets the GoPiGo to manuever automonously"""
        
        #Creates a new empty window on top of the current one
        self.basicObstacleAvoidanceWindow = Toplevel(self.master)
        #Sets the dimensions of the window
        self.basicObstacleAvoidanceWindow.geometry("300x300")
        #Applies the ManualControlApplication framework to the window
        #Note: self.manualControlApp is the object for the ManualControlApplication class
        self.basicObstacleAvoidanceApp = BasicObstacleAvoidanceApplication(self.basicObstacleAvoidanceWindow)
        #Handles the closing of the window, ending the program
        #self.basicObstacleAvoidance.protocol("WM_DELETE_WINDOW",self.manualControlCloseApplication)

#----------
#Node based pathfinding class
#----------
class NodeBasedPathfinding(Frame):
    """Takes the input of points and neighbors, finds the shortest distance from one point to the other ones and moves the robot along the shortest path"""
    def __init__(self,master):
        super(NodeBasedPathfinding, self).__init__(master)
        #Create private fields
        #Holds the text input for the single node inputted
        self.__nodeIn = ""
        #Holds the relative neighbors for the node inputted
        self.__neighborsIn = ""
        self.indexNodeX = 0
        self.indexNodeY = 0
        self.convertedNodeArray = []
        
        #holds the points as single numbers for display
        self.__nodeX = []
        self.__nodeY = []
        #-----------
        #Create objects
        #-----------
        #Create the mapper to convert normal data to be useable by the algorithm
        self.__nMapper = map()
        
        #Positioning used to place widgets
        self.grid()
        #Run the function to setup the widgets on the screen
        self.createWidgets()
        
        #Creates a label object
        self.lblTitle = Label(self, text="Node Based Pathfinding")
        #Applies the grid to the object allowing it to be positioned
        self.lblTitle.grid(row = 0, column = 0, sticky = W)
        
    


    #Creates widgets on the window frame
    def createWidgets(self):
        
        #Accept button to put in a node
        self.btnInputNode = Button(self, text = "Add Node Using Coordinates Relative to The Origin in Inches", command = self.inputNode)
        self.btnInputNode.grid(row = 3, column = 0, sticky = NSEW)
        #Button to run the node through the algorithm
        self.btnRunAlgorithm = Button(self, text = "Calculate shortest paths", command = self.calculatePath)
        self.btnRunAlgorithm.grid(row = 0, column = 3)
        
        #holds the user input for points
        self.entryPoint = Entry(self)
        self.entryPoint.grid(row = 2, column = 0, sticky = NSEW)
        
        self.entryNeighbors = Entry(self)
        self.entryNeighbors.grid(row = 2, column = 2, sticky = NSEW)
        
        #Reads the selected file from __readFile
        self.btnReadFromFile = Button(self, text = "Read from file", command = self.readFromFile)
        self.btnReadFromFile.grid(row = 4, column = 0, sticky = NSEW)
        
        #Writes to selected file
        self.btnReadFromFile = Button(self, text = "Write to file", command = self.writeToFile)
        self.btnReadFromFile.grid(row = 1, column = 3, sticky = NSEW)

        
    #----------
    #Event handlers
    #----------
    def calculatePath(self):
        #Takes all the numbers stored and passes them through Dijkstra's algorithm

        self.__dijkstra = Dijkstras(self.__nMapper.getNode(), self.__nMapper.getNodeNeighbors(), "0,0")
        self.__dijkstra.algorithm()
        print("prev: ", self.__dijkstra.getPrev())
        print("Visited: ", self.__dijkstra.getVisited())
        
              
        
        #Display using MatPlotLib
        plt.scatter(self.__nodeX, self.__nodeY,s= 10, c=(0,0,0),alpha = .5)
        plt.title('Scatter plot')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        
    def inputNode(self):
        """
        Takes data from entryPoint and entryNeighbor and turns them into a readable set of data by the code
        Example input: entryPoint: (0,0) entryNeighbors: (0,1),(1,0)
        """
        
        #Issue: current program only retains the correct format if less than one node is inputted.
        
        #Get input
        self.__nodeIn = self.entryPoint.get()
        self.__neighborsIn = self.entryNeighbors.get()
        
        
        
        #Convert node input to tuple
        self.convertedNode = eval(self.__nodeIn)
        #Convert neighbor input to tuple
        self.convertedNeighbors = eval(self.__neighborsIn)
        #Convert tuple to list
        
        self.convertedNeighbors = list(self.convertedNeighbors)
        self.convertedNeighbors = eval(self.__neighborsIn)
        #Convert tuple to list
        #self.convertedNeighbors = list(self.convertedNeighbors)
        

            
        
        #Go through each node inputed and convert to a readable input by the algorithm
        for i in range(len(self.convertedNeighbors)):
            self.convertedNodeArray.append(list(self.convertedNeighbors[i]))
        
        #Pass through the node mapper to convert it to a dictionary
        self.__nMapper.addNode(self.convertedNode[0], self.convertedNode[1], self.convertedNodeArray)
        print(self.__nMapper.getNodeNeighbors())
        print("getNode(): ", self.__nMapper.getNode())
        

        
        #Add the point to the array
        self.__nodeX.append(self.convertedNode[0])
        self.__nodeY.append(self.convertedNode[1])


    
    #Takes a file from __readFile and loads it into 
    def readFromFile(self):
        self.__file = open("Node.txt", "r")
        
        for line in self.__file:
            print (line)
            
        self.__file = open("NodeNeighbor.txt", "r")
        for line in self.__file:
            print(line)

    def writeToFile(self):
        self.__nMapper.compileMap()
        #Open in overwrite mode
        self.__file = open("Node.txt", "w+")
        #Dump the data to the file
        self.__file.write(json.dumps(self.__nMapper.getNode()))
        self.__file.close()
        
        #Open in append mode
        self.__file = open("NodeNeighbor.txt", "w")
        
        print("nodeNeighbors ", " ".join(self.__nMapper.getNodeNeighbors()))
        
        #Dump the data
        self.__file.write(json.dumps(self.__nMapper.getNodeNeighbors()))
        self.__file.close()

#------------------
#Obstacle avoidance class
#------------------

class ObstacleAvoidanceApplication(Frame):
    
    #Constructor
    def __init__(self, master):
        
        #Declare constants
        DETECT_RANGE = 2
        #Import the constructor from the tkinter frame class
        super(ObstacleAvoidanceApplication, self).__init__(master)
        
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
        """Uses the obstacle avoider class to turn detect and avoid an obstacle"""
        self.__obstacleAvoider.obstacleAvoidance()
        #Allows cancellation of the loop through multithreading
        self.__cancelID = self.__master.after(1, self.obstacleAvoidance)
        
    def stop(self):
        self.master.after_cancel(self.__cancelID)
