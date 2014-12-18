import datetime as dt

#This project was taken from the reddit/r/dailyprogrammer post found here: 
#http://www.reddit.com/r/dailyprogrammer/comments/2hcwzn/09242014_challenge_181_intermediate_average_speed/

class highway(speedLimit,cameras=[],cars=[]):
    """
    Creates a highway class that contains a list of cars and cameras
    
    Parameters:
        speedLimit = The speed limit for the highway (Integer)
        cameras = A list of cameras that are stationed along the highway (List)
        cars = A list of cars that were observed on the highway (List)
    """
    self.speedLimit = speedLimit
    self.cameras = cameras
    self.cars = cars
    
    def addCar(car):
        """
        Adds a car to the list of cars on the highway
        
        Parameters:
            car = The license plate for the vehicle to add (String)
        """
        
        if car not in self.cars:
            self.cars.append(car)
            
    def getCars():
        """
        Returns: the list of cars on the highway
        """
        return self.cars

    def addCamera(camera):
        """
        Adds a camera to the list of cameras on the highway
        
        Parameters:
            camera = A camera to be added to the highway (camera Object)
        """
        if camera not in self.cameras:
            self.cameras.append(camera)

    def getCameras():
        """
        Returns: A list of all of the cameras on the highway
        """
        return self.cameras

class camera(name,location):
    self.name = name
    self.location = location
    
    def getLocation():
        """
        Returns: An Int representing the distance the camera is down the highway
        """
        return self.location
    def getName():
        """
        Returns: A String representing the name of the camera
        """
        return self.name
def detectSpeeders(fileName):
    """
    Determines the cars speeding past security cameras on a stretch of 
    highway.
    
    Parameters: 
        fileName = The location of the .txt file that contains all vehicle 
        sightings (String)
        
    Returns:
        A line for each vehicle that has broken the speed limit
        """
        
    speedLimit = 0
    
    #Open the .txt file and add each line to a new location in an array
    with open(fileName,'r',0) as f:
        fileLines = [line.strip() for line in f]

    #for line in fileLines:
        
        


target = "C:\Users\Mike\Google Drive\Programming Projects\Programming-Projects\Average_Speed_Test_Data.txt"    

detectSpeeders(target)