#Filename: Main.py
#Author: Daniel Smith


#Import the gui library
from tkinter import *
#Import the class that runs the main application
from Application import Application

#Define constants
MAIN_TITLE = "GoPiGo Control Program"
MAIN_DIMENSION = "500x300"

#Setup Objects
root = Tk()

#Event handling for when the root application closes
def onClosing():
    root.destroy()

#Contains the executable code
def Main():
    #General Exception
    
    
    #Defines settings for the base window
    root.title(MAIN_TITLE)
    root.geometry(MAIN_DIMENSION)
    #Loads the framework into the window
    app = Application(root)
    #Defines the protocol for closing a window
    root.protocol("WM_DELETE_WINDOW", onClosing)
    #Runs the main loop for the application
    app.mainloop()
 
#Run the program
Main()

