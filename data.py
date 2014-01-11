# Database module

##import main
##import user
##import joy
'''
 

+class competition:

+    def __init__(numMatches, name):

+        #if numMatches = 0 then number of matches in competician is unknown

+        #name is a name given for this competitian ex) 'FLR seeding', 'FLR final', 'nationals Finals'

+        matchList[]

+        matchlist.append(0)

+    def newMatch(robots):

+        matchList[0] += 1

+        matchlist.append(match(self, matchList[0], robots))

'''

class Competition(list):
    
    def __init__(self, numberOfMatches=0, name="Test"):
        # If numMatches = 0 then number of matches in competician is unknown
        # name is a name given for this competitian ex) 'FLR seeding', 'FLR
        # final', 'nationals Finals'
        self.name = name
<<<<<<< HEAD
        self.current_match = 0
        self.last_match = 0
=======
        self.numMatches = numberOfMatches
>>>>>>> 4abbc335e276a7fd742987496ce89e22740b2d55
        
    def newMatch(self, teamNumbers):
        # New Match takes a list of robot numbers as an argument
<<<<<<< HEAD
        ##self[0] += 1
        self.append(Match(self.last_match, teamNumbers))
        self.last_match += 1

=======
        self.inMatches=len(self)+1
        self.append(Match(self.inMatches, robots, self.name))
        
>>>>>>> 4abbc335e276a7fd742987496ce89e22740b2d55
    def editMatch(self, matchNumber, teamNumbers):
        self[matchNumber-1] = Match(self.last_match, teamNumbers)




# an instance of a match with a number and six robot objects
class Match:
    
    def __init__(self, num, teamNumbers, compName):
        self.comp = compName
        self.number = num
        self.robots = [] # [0:2] red, [3:5] blue
        i = 0
        for teamNumber in teamNumbers:
            # This will create a new robot each time it is called,
<<<<<<< HEAD
            # We don't want that to happen for existing robots
            self.robots[i] = RobotMatchPerformance(teamNumber, self, i)
            i += 1
            	

=======
            robots[n] = InMatchRobot(teamNumber,self, n, self.comp)
            n += 1  # [0:2] red, [3:5] blue
            pass
        
'''
>>>>>>> 4abbc335e276a7fd742987496ce89e22740b2d55
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


def getRobot(self, teamNumber):
# Get a robot specified by it's id (number)
pass

def removeRobot(self, robot):
# Try statement scheduled to be removed, will take care of error handly in Form
try: self.remove(robot)

except:
"I need to look up what goes here"
pass

def removeTeamNumber(self, teamNumber):
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

'''
        
# An instance of a robot in one match in one competician, will be diffent for the same teams robot in diffent matches and competicians
class InMatchRobot:
    
    def __init__(self, teamNumber, myMatch, num, compName):
        self.comp = compName
        self.match = myMatch
        self.teamNumber = teamNumber
        self.num = num
        if allianceNumber < 3:
            self.alliance = 'RED'
        else:
            self.alliance = 'BLUE'

<<<<<<< HEAD
        self.matchHistory[matchNumber] = [matchNumber, alliance]
        
        ##records = RobotRecords(Match.comp.name,myMatch.matchNum,alliance)

class RobotMatchPerformacne():

    def __init__(self, teamNumber, myMatch, num):
        # I don't know what comp does, and it isn't used in the program
        pass
			
class RobotRecords:
    def __init__(self, comp, myMatch, robot, alliance):
=======
        records = InMatchRobotRecords(comp,self.match,self.teamNumber,self.alliance)

                        
class InMatchRobotRecords:
    def __init__(self, compName, myMatch, robot, ally):
        self.comp = compName
        self.match = myMatch
        self.roboNum = robot
        self.alliance = ally # string (RED or BLUE)
        
        
>>>>>>> 4abbc335e276a7fd742987496ce89e22740b2d55
        pass
        # variables being recorded ex)shots missed, points scored, climberlevel reached
                
