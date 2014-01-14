

class RobotList(list):
"""This class inherits from the list class, it will handle all robot objects"""
    def __init__(self):
        self.current_robot_index = 0
        self.robotKeys = []


    def __str__(self):
        return str([robot.teamNumber for robot in self])

    def addRobot(self, robot):
        """
        if the list is empty it just adds the robot, like wise if it is
        the largest member of the list. Otherwise it places the robot before
        the next greatest number through a binary search
        """
        #at this point if two different robots share the same number,
        #it will try to add the robot, but may end up freaking out.
        if robot in self:
            return False
        elif self == []:
            self.append(robot)
        elif robot.teamNumber >= self[-1].teamNumber:
            self.append(robot)
        else:
            index = self._binSearchIndex(robot.teamNumber)
            self.insert(index, robot)
            self.robotKeys = [robot.teamNumber for robot in self]
        # Update the key List
        return True

    
    def _binSearchIndex(self, teamNumber):
        # After much consternation this works!, it returns the index of the lowest
        # roboNum above the given one
        import math
        tmpRoboList = self[:]
        while len(tmpRoboList) != 1:
            tmpIndex = math.ceil(len(tmpRoboList)/2) - 1 #Splits the list in half, bias towards lower number
            if teamNumber < tmpRoboList[tmpIndex].teamNumber:
                tmpRoboList = tmpRoboList[:(tmpIndex+1)]
            elif teamNumber > tmpRoboList[tmpIndex].teamNumber:
                tmpRoboList = tmpRoboList[(tmpIndex+1):]
                
        return self.index(tmpRoboList[0])
        # Returns the index of the robot just greater than the tested one, I hope


    def removeTeamNumber(self, teamNumber):
        # Removes a robot based on it's number
        robotVar = self.getRobot(teamNumber)
        self.removeRobot(robotVar)

    def removeRobot(self, robot):
        # Try statement scheduled to be removed, will take care of error handly in Form
        try: self.remove(robot)

        except:
            "I need to look up what goes here"
        pass

    def getRobot(self, teamNumber):
        # Get a robot specified by it's id (number)
        pass
        
        #edit this to instead mark a robot as removed so that it can easily be recreated
        #make a reset robot match data

    
class Robot():
     def __init__(self, teamNumber):
        self.teamNumber = teamNumber
        self.matches = [] # has robo record files 
        #self.__deleted = False
     
    def addMatch(self, records) 
        self.matches.append(records)
        
        
     
        
