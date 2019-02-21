
#Import libraries
import logging
try:
    import easygopigo3 as easy
except ImportError as e:
    logging.exception("Failed to import the easygopigo3 library")
except Exception as e:
    logging.exception("Something went wrong with the easygopigo3 library")
    
#The main class
class RobotController:
    """
    This class contains multiple nested classes which allows for easy control of the robot
    """
    def __init__(self):
        #A single gopigo control object to be used by all classes
        self.__gpgMain = easy.EasyGoPiGo3()
        
        self.movementControl = self.MovementControl(self.__gpgMain)
        self.deadReckoning = self.DeadReckoning(self.__gpgMain)
        self.distanceSensor = self.DistanceSensor(self.__gpgMain)
    
    class MovementControl:
        """
        This subclass controls the gopigo robot by creating endless movement.
        
        Call setDirection("Stop") to stop the robot
        """
        
        def __init__(self, gpg):
            """
            Sets up the fields to control the robot
            """
            try:
                #Sets default speed
                self.__speed = 100
                #Sets the direction to stopped
                self.__direction = "Stop"
                #GoPiGo controller object
                self.__gpg = gpg
            except Exception as e:
                logging.exception("Error initializing object")
            
        def setDirection(self, direction):
            
            """
            Sets the direction the robot moves in until it is told to stop
            Accepts "Forward" "Backward" "Right" "Left" and "Stop" as input
            """
            self.__direction = direction
            #Test for direction, includes exception handling
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
                logging.exception("Something went wrong when attempting to set the directino of the robot")
        
        #TODO: Reimplement at the top level
        #Sets the speed of the robot
        def setSpeed(self, speed):
            try:
                #Sets the speed field
                self.__speed = self.speed
                #Updates the robot speed
                self.__gpg.set_speed(self.__speed)
            except Exception as e:
                logging.exception("Failed setting the speed of the robot")
            
    class DeadReckoning:
        """
        This subclass contains functions that will move the robot forward a set distance.
        All functions are set to blocking mode which will prevent simmilar functions from overriding a previous function until it has finished
        The turning functions are a tank turn where the robot stays in the same place and moves one wheel forward and the other backwards
        Measurments are in inches and degrees
        """
        
        def __init__(self, gpg):
            try:
            #Initialize an easygopigo from the top class
                self.__gpg = gpg
            
                #Sets default speed
                self.__speed = 100
                self.__degrees
                self.__inches
                #GoPiGo controller object
            except Exception as e:
                logging.exception("Failed to initialize")
        
        def moveForward(self, inches):
            """Moves the robot a certain amount in inches"""
            self.__inches = inches
            self.__gpg.drive_inches(self.__inches, blocking=True)
        
        
        def moveBackward(self, inches):
            
            """Moves the robot backwards a certain amount of inches by inverting the input"""
            self.__inches = inches
            self.__gpg.drive_inches((-1 * self.__inches), blocking=True)
        
        def moveRight(self, degrees):
            
            """Turns the robot right using a tank turn and a certain amount of degrees"""
            self.__degrees = degrees
            self.__gpg.turn_degrees(self.__degrees, blocking=True)    
        
        def moveLeft(self, degrees):
   
            """Turns the robot left using a tank turn and a certain amount of degrees inverted""" 
            self.__degrees = degrees
            self.__gpg.turn_degrees((-1 * self.__degrees), blocking=True)
            
            #TODO: Reimplement this on the top level        
        def setSpeed(self, speed):
            """Sets the speed of the robot"""
            try:
                #Sets the speed field
                self.__speed = self.speed
                #Updates the robot speed
                self.__gpg1.set_speed(self.__speed)
            except Exception as e:
                logging.exception("Failed setting the speed of the robot")
        
        def getSpeed(self):
            return self.__speed
        
    class DistanceSensor():
        """
        Controls the distance sensor module
        Note: The distance sensor must be installed on an Ic2 port to work
        """
        def __init__(self, gpg):
            self.__port = "I2C"
            #Private objects
            #Robot controller
            self.__gpg = gpg
            #Distance sensor controller
            self.__distanceSensor = self.__gpg.init_distance_sensor(port = self.__port)
            
        def getDistance(self):
            """Reads the distance from the distance sensor and outputs it in inches"""        
            return self.__distanceSensor.read_inches()