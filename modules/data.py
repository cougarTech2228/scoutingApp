# Database module

"""
class CompetitionList(list):
    def __init__(self, test=False):
        self.test = test
        if self.test is True:
            self.addComp("Test")

    def addComp(self, name):
        self.append(Competition(name))
"""

class Competition(list):

    def __init__(self, name = "test", numberOfMatches=0):
        # If numMatches = 0 then number of matches in competician is unknown
        # name is a name given for this competitian ex) 'FLR seeding'
        self.name = name
        #self.current_match = 0
        #self.last_match = 0
        self.numMatches = numberOfMatches

    def newMatch(self, matchNum=None, force =False): #matchNum starts at 1 not o
        # New Match takes a list of robot numbers as an argument

        self.inMatch = len(self)
        #inmatch is the # of inputed matches
        if matchNum is None:
            index = len(self)
        else:
            index = matchNum-1
            
        print ("creating match #",matchNum)

        try:
            if self[index]:
                print("match already exists")
                if not force:
                    print("aborting")
                    return
                else:
                    print("forcing  override")
                    
            elif self[index] == None:
                print("match already allocated - creating match")
            self[index] = Match(self.inMatch+1)       
            print("match created")   
            
        except IndexError:
            for x in range(matchNum - self.inMatch):
                print("allocatingMatch")    
                self.append(None)
            self[index] = (Match(matchNum))
            print("match created")
            #print(self)
            
    def editMatch(self, matchNumber):
        self[matchNumber-1] = Match(matchNumber-1)



# an instance of a match with a number and six robot objects
class Match:

    def __init__(self, matchNum):
        self.notRun = True
        self.number = matchNum
#        self.robots = [None, None, None, None, None] # [0:2] red, [3:5] blue
        self.robots = dict()
        """
        n = 0
        for teamNumber in teamNumbers:
            # This will create a new robot each time it is called

            self.robots[n] = InMatchRobot(teamNumber, n)
            n += 1  # [0:2] red, [3:5] blue
        """

class InMatchRobotRecords:
    def __init__(self,myMatch, robot, ally):

        self.match = myMatch #match object
        self.teamNumber = robot #robot number
        self.alliance = ally # string (RED or BLUE)
        self.comments = []
        self.records =  dict([])
        self.points = 0        
    

#---------------------------------------------------------------------------------


#Stored data
# Database module

#from events import *
# forgive me but it was driving me crazy with the events objects in this module,
# probably the opposite of your feeling (this line should take care of any issues right)


class RobotList(dict):
    """This class inherits from the list class, it will handle all robot objects"""
    def __init__(self):
        pass

    def __str__(self):
        return list(self.keys())


    def addRobot(self, robot):
        """
        if the list is empty it just adds the robot, like wise if it is
        the largest member of the list. Othderwise it places the robot before
        the next greatest number through a binary search
        """
        add_robot = True
        for r in self:
            if r == robot.teamNumber:
                add_robot = False
                break
        if add_robot is True:
            self[robot.teamNumber] = robot
            


    def removeRobot(self, robot):
        # Try statement scheduled to be removed, will take care of error handly in Form
        try:
            tmp_deleted = None
            for robotNum in self:
                if robotNum == robot.teamNumber:
                    del(self[robot.teamNumber])
                    break
                
        except ValueError: 
            print('Sorry need to check what goes here')

    def getRobot(self, teamNumber):
        # Get (a robot specified by it's id (number)
        try:
            return self[teamNumber]
            
        except ValueError:
            print("I don't even think this is the right error")

        #edit this to instead mark a robot as removed so that it can easily be recreated
        #make a reset robot match data

    def removeTeamNumber(self, teamNumber):
        # Removes a robot based on it's number
        try:
            self.removeRobot(self[teamNumber])
            
        except:
            print('bollocks')

##    def _binSearchIndex(self, teamNumber):
##        # After much consternation this works!, it returns the index of the lowest
##        # roboNum above the given one
##        import math
##        tmpRoboList = self[:]
##        while len(tmpRoboList) != 1:
##            tmpIndex = math.ceil(len(tmpRoboList)/2) - 1 #Splits the list in half, bias towards lower number
##            if teamNumber < tmpRoboList[tmpIndex].teamNumber:
##                tmpRoboList = tmpRoboList[:(tmpIndex+1)]
##            elif teamNumber > tmpRoboList[tmpIndex].teamNumber:
##                tmpRoboList = tmpRoboList[(tmpIndex+1):]
##
##        return self.index(tmpRoboList[0])
##        # Returns the index of the robot just greater than the tested one, I hope



class Robot():
    def __init__(self, teamNumber):
        self.teamNumber = teamNumber
        self.matches = []#this points to  "inMatchRobotRecords" object
        self.totalPts = 0
        self.specifications = pitScout()
        self.comments = []
        # has robo record files
        #self.__deleted = False

    def addMatch(self, records):
        self.matches.append(records)

    def calculateStats(self):
        self.totalPts = 0
        for record in self.matches:
            for event in record.events:
                self.totalPts += event.pointsValue

    def getAvgPoints(self):
        return self.totalPts/len(self.matches)

class Comment():
    def __init__(self,title, description="",ranking=None):
        self.title = title
        self.description=description
        self.ranking = ranking
        
class pitScout():
    def __init__(self):
        pass
    
