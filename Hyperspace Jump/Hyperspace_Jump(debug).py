import networkx as nx
import matplotlib.pyplot as plt


#This project was taken from the reddit/r/dailyprogrammer post found here: 
#http://www.reddit.com/r/dailyprogrammer/comments/2fe72z/9032014_challenge_178_intermediate_jumping/

#Function to draw a graphical representation of space
def drawGraph(space):
    """
    Displays an edge and node graph to represent all of the planets in space 
    and their possible paths
    
    Parameters:
        space: a graph of all planets(nodes) and paths (edges) (digraph)
        
    Returns:
        A figure
    """
    pos = nx.spring_layout(space)
    nx.draw_networkx_nodes(space,pos)
    eone = [(u,v) for (u,v,d) in space.edges(data=True) if d['fuel']==1]
    etwo = [(u,v) for (u,v,d) in space.edges(data=True) if d['fuel']==2]
    ethree = [(u,v) for (u,v,d) in space.edges(data=True) if d['fuel']==3]
    efour = [(u,v) for (u,v,d) in space.edges(data=True) if d['fuel']==4]
    nx.draw_networkx_edges(space,pos,edgelist=eone,width=2,edge_color='green')
    nx.draw_networkx_edges(space,pos,edgelist=etwo,width=3,edge_color='blue')
    nx.draw_networkx_edges(space,pos,edgelist=ethree,width=4,edge_color='orange')
    nx.draw_networkx_edges(space,pos,edgelist=efour,width=5,edge_color='red')
    nx.draw_networkx_labels(space,pos)
    plt.axis("off")

    plt.show()
    

def getDeepest(planets):
    """
    Compares different planets (nodes) and returns the planet (node) that 
    is farthest away.
    
    Parameters:
        planest: All the planets to compare (list[string])
        
    Returns:
        The node that is the farthest away (string)
    """
    farthest = planets[0]
    #Compare each planet to every other planet in the list, excluding all preceeding planets
    for i in range(len(planets)):
        if planets[i]>farthest:
            farthest = planets[i]
    return farthest
    
def checkOverlap(path,node1,node2):
    """
    Looks through the path to make sure the trip from node1 to node2 or vice versa
    has not been taken yet
    
    Parameters: 
        path: The path of all planets already visited (list[String])
        node1, node2: The two planets whose path is to be considered (String)
        
    Returns:
        True if Overlap has been found, False otherwise (boolean)
    """
    currentPath = [node1,node2]
    for i in range(len(path)-1):
        if [path[i],path[i+1]]== currentPath or [path[i+1],path[i]]==currentPath:
            return True
    return False
    
def DepthFirstSearch(space, startingPlanet, currentPlanet, fuelTank, path=[],deepestPath=None,deepestPlanet=None):
    """
    Uses depth first search to return all possible paths that result in returning home
    
    Parameters:
        space: a digraph of planets(nodes) and paths (edges) (digraph)
        startingPlanet: the starting planet (node)
        currentPlanet: the current plante (node)
        fuelTank: the amount of fuel remaining (integer)
        path: the current path (list)
        deepestPath: The deepest path that has been found so far (list)
        
    Returns:
        a list of the deepest path possible with the fuel available (list[String])
    """
    path = path+[currentPlanet]
    
    #If you have returned to home planet, return the deepest path thus far
    if currentPlanet == startingPlanet and fuelTank >=0 and len(path)>1:
        #look for deepest planet in current path and compare to deepest known planet
        #print "We have returned home through the path: ",path
        deepPlanet = getDeepest(path)
        print "Comparing the deepest planet ",deepPlanet, "from path: ",path, "to current deepest Planet ",deepestPlanet
        if getDeepest([deepPlanet,deepestPlanet])==deepPlanet or deepestPath==[]:
            print "Setting the deepestPlanet to ",deepPlanet," through the path ",path
            deepestPlanet = deepPlanet
            deepestPath = path
        return deepestPath
            
    print "Iteration through planets from planet  (",currentPlanet,") with the current path: ",path
    for planet in space[currentPlanet]:
        remainingFuel = fuelTank-space[currentPlanet][planet]['fuel']
        print "Fuel remaining after traveling to planet ",planet," from ",currentPlanet," is ",remainingFuel
        if not checkOverlap(path,currentPlanet,planet) and remainingFuel>=0:
            print "Recursively searching through paths from Planet ",planet," and the current deepest path is ",deepestPath
            newDeepPath = DepthFirstSearch(space,startingPlanet,planet,remainingFuel,path,deepestPath,deepestPlanet)
            if newDeepPath !=None:
                deepPlanet = getDeepest(newDeepPath)
                print "Comparing the deepest planet ",deepPlanet, "from path: ",newDeepPath, "to current deepest Planet ",deepestPlanet
                if getDeepest([deepPlanet,deepestPlanet])==deepPlanet or deepestPlanet==None:
                    print "Setting the deepestPlanet to ",deepPlanet," through the path ",newDeepPath
                    deepestPlanet = deepPlanet
                    deepestPath = newDeepPath

    return deepestPath      
            
def findDeepestRoute(fuelTank):
    """
    Finds the deepest planet that can be reached using the fuel allowed through 
    brute force, depth first search
    
    Parameters:
        fuelTank: Total amount of fuel available to use (integer)
        
    Returns:
        The deepest path that uses the most fuel possible without repeating any 
        steps in the path.
    """
    space = nx.Graph()
    #List of all possible paths (edges) along with fuel cost
    paths = [('A','B',{'fuel':1}),('A','C',{'fuel':1}),('B', 'C',{'fuel':2}),('B', 'D',{'fuel':2})\
    , ('C', 'D',{'fuel':1}),('C', 'E',{'fuel':2}),('D','E',{'fuel':2}),('D','F',{'fuel':2})\
    ,('D','G',{'fuel':1}),('E','G',{'fuel':1}),('E','H',{'fuel':1}),('E','H',{'fuel':1})\
    ,('F','I',{'fuel':4}),('F','G',{'fuel':3}),('G','J',{'fuel':2}),('G','H',{'fuel':3})\
    ,('H','K',{'fuel':3}),('I','J',{'fuel':2}),('I','J',{'fuel':2}),('I','K',{'fuel':2})]
    #Adding all planets and paths
    space.add_edges_from(paths)

    #drawGraph(space)
    
    path = DepthFirstSearch(space,'A','A',fuelTank)
    return path
 
ans = findDeepestRoute(5)



