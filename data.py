# Database module

from sData import *


class Data(): #through this class all of data will be accessed This might go in main (probably)
    def __init__(self): #reminder -this must be fixed
        self.CompList = CompeticianList()
        self.Robots = RobotList()
        pass
    
class CompeticianList(list):
    def addComp(self, name):
        self.append(Competition(name))


class Competition(list):
    
    def __init__(self, numberOfMatches=0, name="Test"):
        # If numMatches = 0 then number of matches in competician is unknown
        # name is a name given for this competitian ex) 'FLR seeding', 'FLR
        # final', 'nationals Finals'
        self.name = name
        self.current_match = 0
        self.last_match = 0
        self.numMatches = numberOfMatches
        
    def newMatch(self, teamNumbers):
        # New Match takes a list of robot numbers as an argument
        ##self[0] += 1
        self.append(Match(self.last_match, teamNumbers))
        self.last_match += 1
        self.inMatches=len(self)+1
        #inmatches is the #of inputed matches
        self.append(Match(self.inMatches, robots, self.name))

    def editMatch(self, matchNumber, teamNumbers):
        self[matchNumber-1] = Match(self.last_match, teamNumbers)



# an instance of a match with a number and six robot objects
class Match:
    
    def __init__(self, num, teamNumbers, compName):
        self.events = evtList()
        self.comp = compName
        self.number = num
        self.robots = [] # [0:2] red, [3:5] blue
        self.events = GameEventList()
        i = 0
        for teamNumber in teamNumbers:
            # This will create a new robot each time it is called,
            # We don't want that to happen for existing robots
            self.robots[i] = RobotMatchPerformance(teamNumber, self, i)
            i += 1
            robots[n] = InMatchRobot(teamNumber,self, n, self.comp)
            n += 1  # [0:2] red, [3:5] blue
            pass
        
    def addEvent(robot, event)
        #this will need to add event to match evt list and robot records evt list
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
        # this does not belong here - self.matchHistory[matchNumber] = [matchNumber, alliance]
        
        self.records = RobotRecords(Match.comp.name,myMatch.matchNum,alliance) # this should be in match robot records
        
    def addEvent(event):
        add event to InMatchRobotRecords
        
                
class InMatchRobotRecords:
    def __init__(self, compName, myMatch, robot, ally):
        self.comp = compName #compatician name
        self.match = myMatch #match object
        self.roboNum = robot
        self.alliance = ally # string (RED or BLUE)
        self.events = GameEventList()
        # variables being recorded ex)shots missed, points scored, climberlevel reached



    
