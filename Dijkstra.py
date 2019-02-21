#Filename: Dijkstra.py
#Author: Daniel Smith

import math
import logging
class Dijkstras:
    def __init__(self, nodeMap, neighborMap, startPos):
        """
        This class returns the shortest distance from a list of point and their neighbors
        
        Input types:
        nodeMap example:
        ('0,0','1,0','0,1','1,2', '1,3')
        
        
        neighborMap example:
        {
        '0,0': {'0,1': 1.0, '1,0': 1.0}, 
        '0,1': {'0,0': 1.0, '1,2': 1.4142135623730951}, 
        '1,0': {'0,0': 1.0, '1,2': 2.0}, 
        '1,2': {'0,1': 1.4142135623730951, '1,0': 2.0, '1,3': 1.0}, 
        '1,3': {'1,2': 1.0}
        }
        startPos example:
        '0,0'
        """
        #Declare fields
        #The starting position for the algorithm
        self.__start = startPos
        self.__neighbors = neighborMap
        self.__nodes = nodeMap
        self.__visited = {}
        self.__prev = {}
    
    def algorithm(self):
        ######Djikstra's Logrithm######
        #See: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
        #Set all nodes distance to infinity
        print("Neighbors")
        print(self.__neighbors)
        print("Nodes")
        print(self.__nodes)
        unvisited = {n: math.inf for n in self.__nodes}
        #Set the starting node's distance to 0
        unvisited[self.__start] = 0
        #Empty visited list which will contain the visited nodes
        print(unvisited)
        #While the unvisited set contains data
        while unvisited:
            #Sets minNode to the key of the smallest distance
            minNode = min(unvisited, key = unvisited.get)
            #gets the neighbors of each point by going into the subkey and finding the values for each
            for neighborCounter in self.__neighbors[minNode].keys():
                #Sets a temporary cumulative distance
                tempDistance = unvisited[minNode] + self.__neighbors[minNode][neighborCounter]
                try:
                    #If the temp distance is less than the current distance, a shorter path has been found
                    if(tempDistance < unvisited[neighborCounter]):
                        #Set the distance of the neighbor to the new cumulative distance
                        unvisited[neighborCounter] = tempDistance
                        #Set the preview of the path
                        self.__prev[neighborCounter] = minNode
                except Exception:
                    pass
            #Store the node that has been calculated
            self.__visited[minNode] = unvisited[minNode]
            #Get rid of the node that has been calculated
            unvisited.pop(minNode)

        print(self.__prev, self.__visited)
        
    
    def getPrev(self):
        return self.__prev
    def getVisited(self):
        return self.__visited
    
    
    
    def setStartPos(self, start):
        self.__start = start
    def setNeighbors(self, neighbors):
        self.__neighbors = neighbors
    def setNodes(self, nodes):
        self.__nodes = nodes