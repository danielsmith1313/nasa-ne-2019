import math
class map():
    def __init__(self):
        #Holds the converted coordinates of all nodes
        self.__node = ()
        #Holds the coordinates as keys and each neighbor as subkeys containing the calculated distance
        self.__nodeNeighbors = {}
        #Array that holds the nodes to be converted into the tuple
        self.__nodeList = []
    
    def compileMap(self):
        """Called once all nodes have been added to"""
        self.__node = tuple(self.__nodeList)

    #Getters
    def getNode(self):
        return self.__node

    def getNodeNeighbors(self):
        return self.__nodeNeighbors
    
    #Setters
    def setNodeNeighbors(self,nodeIn):
        self.__nodeNeighbors = nodeIn
    def setNode(self, nodeIn):
        self.__node = nodeIn

    def addNode(self, nodeX, nodeY, neighborData):
        """Formats the node map and node neighbor from a x and y initial value and a 2d array of neighbor x and y values
        Example input:
        nMapper = map()
        nMapper.addNode(0,0,[[0,1], [1,0]])
        nMapper.addNode(0,1,[[0,0], [1,2]])
        nMapper.addNode(1,0,[[0,0],[1,2]])
        nMapper.addNode(1,0,[[0,0],[1,2]])
        nMapper.addNode(1,2,[[0,1],[1,0],[1,3]])
        nMapper.addNode(1,3,[[1,2]])
        
        Output:
        nodes = ("0,0","1,0","0,1","1,2", "1,3")

        #Dictionary that represents the nodes and contains the neighbors of each node along with the calculated distance
        nodeNeighbors = {
        '0,0': {'0,1': 1.0, '1,0': 1.0}, 
        '0,1': {'0,0': 1.0, '1,2': 1.4142135623730951}, 
        '1,0': {'0,0': 1.0, '1,2': 2.0}, 
        '1,2': {'0,1': 1.4142135623730951, '1,0': 2.0, '1,3': 1.0}, 
        '1,3': {'1,2': 1.0}
        }
        """

        #Update the node list with the new node
        self.__nodeList.append(str(nodeX) + "," + str(nodeY))

        #Update the neighbor list starting with the first value and calculating the distance of the neighbors
        self.__nodeNeighbors.update({(str(nodeX) + "," + str(nodeY)):{(str(neighborData[0][0]) + "," + str(neighborData[0][1] )): str(self.distance((neighborData[0][0]), (neighborData[0][1]), nodeX, nodeY))}})
        for i in range(len(neighborData)):

            self.__nodeNeighbors[(str(nodeX) + "," + str(nodeY))].update({(str(neighborData[i][0]) + "," + str(neighborData[i][1] )): self.distance((neighborData[i][0]), (neighborData[i][1]), nodeX, nodeY)})
            
        

    def distance(self, x1, y1, x2, y2):
        """Calculates the distance between two coordinate points"""
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return dist
