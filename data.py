# Database module

##import main
##import user
##import joy

class MatchList(list):
    
    def __init__(self, numMatches=0, name="Test"):
        # If numMatches = 0 then number of matches in competician is unknown
        # name is a name given for this competitian ex) 'FLR seeding', 'FLR
        # final', 'nationals Finals'
        self.name = name
        self.current_match = 0
        self.last_match = 0
        ##self.append(0)
        
    def newMatch(self, robots):
        # New Match takes a list of robot numbers as an argument
        ##self[0] += 1
        self.append(Match(self.last_match, teamNumbers))

    def editMatch(self, matchNumber, teamNumbers):
        self[matchNumber-1] = Match(self.last_match, teamNumbers)




# an instance of a match with a number and six robot objects
class Match:
    
    def __init__(self, num, teamNumbers):
        self.number = num
        self.robots = [] # [0:2] red, [3:5] blue
        n = 0
        for teamNumber in teamNumbers:
            # This will create a new robot each time it is called,
            # We don't want that to happen for existing robots
            ##robots[n] = Robot(teamNumber, n)
            ##n += 1
            pass
	

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
        the largest member of the list.  Otherwise it places the robot before
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


    def getRobot(self, teamNumber):
        # Get a robot specified by it's id (number)
        pass

    def removeRobot(self, robot):
        # Try statement scheduled to be removed, will take care of error handly in Form
        try: self.remove(robot)

        except:
            "I need to look up what goes here"
            pass

    def removeteamNumber(self, teamNumber):
        # Removes a robot based on it's number
        robotVar = self.getRobot(teamNumber)
        self.removeRobot(robotVar)

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


	
# An instance of a robot object, generally handled by RobotList object, represents a Team's robot
class Robot:
    
    def __init__(self, teamNumber):
        self.teamNumber = teamNumber
        self.matchHistory = {}

    def updateHistory(matchNumber, allianceNumber):
        if allianceNumber < 3:
            alliance = 'RED'
        else:
            alliance = 'BLUE'

        self.matchHistory[matchNumber] = [matchNumber, alliance]

        

        
        ##records = RobotRecords(Match.comp.name,myMatch.matchNum,alliance)

			
class RobotRecords:
    def __init__(self, comp, myMatch, robot, alliance):
        pass
        # variables being recorded ex)shots missed, points scored, climberlevel reached
                
