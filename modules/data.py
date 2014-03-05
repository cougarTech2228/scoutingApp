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

    def newMatch(self, teamNumbers, matchNum=None, force =False): #matchNum starts at 1 not o
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
            self[index] = Match(self.inMatch+1, teamNumbers, self)       
            print("match created")   
            
        except IndexError:
            for x in range(matchNum - self.inMatch):
                print("allocatingMatch")    
                self.append(None)
            self[index] = (Match(matchNum, teamNumbers, self))
            print("match created")
            #print(self)
            
    def editMatch(self, matchNumber, teamNumbers):
        self[matchNumber-1] = Match(matchNumber-1, teamNumbers, self)



# an instance of a match with a number and six robot objects
class Match:

    def __init__(self, matchNum, teamNumbers, comp):
        self.notRun = True
        self.comp = comp
        self.number = matchNum
#        self.robots = [None, None, None, None, None] # [0:2] red, [3:5] blue
        self.events = GameEventList()
        self.robots = [ InMatchRobot(teamNumbers[n], n, self) for n in range(len(teamNumbers))] #Python Magic 
        """
        n = 0
        for teamNumber in teamNumbers:
            # This will create a new robot each time it is called

            self.robots[n] = InMatchRobot(teamNumber, n)
            n += 1  # [0:2] red, [3:5] blue
        """


class InMatchRobot:

    def __init__(self, teamNumber, num, match):
        self.match = match
        self.teamNumber = teamNumber
        self.allianceNumber = num
        self.records = None
        if self.allianceNumber < 3:
            self.alliance = 'RED'
        else:
            self.alliance = 'BLUE'
        # this does not belong here - self.matchHistory[matchNumber] = [matchNumber, alliance]




class InMatchRobotRecords:
    def __init__(self, compName, myMatch, robot, ally):
        self.comp = compName #compatician name
        self.match = myMatch #match object
        self.teamNumber = robot #robot number
        self.alliance = ally # string (RED or BLUE)
        self.events = GameEventList() 
        self.comments = []
        self.records =  dict([])#dictionary of evt types with lists of failures and successes
        # variables being recorded ex)shots missed, points scored, climberlevel reached
        self.points = 0        
        
    def addEvt(self, event):
        print("adding event in matchrobot records")
        self.events.add(event)
        pass
        #add event to event list

    def tally(self):
        print("going to tally events")
        for evt in self.events.getMainList():
            print("there actually is an event")
            if not evt.__class__.__name__ in self.records:
                self.records[evt.__class__.__name__]=[0, 0] #failures and successes
                print("created list for ", evt.__class__.__name__)
                
            if evt.success:
                self.records[evt.__class__.__name__][1] += 1
                print("success event in ", evt.__class__.__name__)
            else:
                print("failure event in ", evt.__class__.__name__)
                self.records[evt.__class__.__name__][0] += 1
                    
            self.points += evt.pointsValue

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


    def add(self, robot):
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
                    del(self[teamNumber])
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




#----------------------------------------------------------------------------------


# The Game Event List is the log of all events that the user inputs, since each
# Game event objecct points to the one before it, there is no need to order it.
# That is, each event can simply be added to the end of the list
class GameEventList(list):
    # When the list is created it adds a start event, so that the first added
    # event will have something to point to
    def __init__(self):
        self.eventIndexCounter = -1
        self.HEAD = None
        self.add(StartEvent())


    def add(self, event):
        print("adding event to list")
        self.append(event)
        # Have the old event point to the added event
        # and the new event point to the preceding event

        event.setPrecedingEvent(self.HEAD)

        # This block is only going to be applicable to the StartEvent

        if event.precedingEvent is not None:
            self.HEAD.setAntecedingEvent(event)
        self.eventIndexCounter += 1
        self.HEAD = self[self.eventIndexCounter]

    def undo(self):
        if self.HEAD.precedingEvent is not None:
            self.HEAD = self.HEAD.precedingEvent

    def redo(self):
        if self.HEAD.antecedingEvent is not None:
            self.HEAD = self.HEAD.antecedingEvent

    # getMainList returns a list starting at head, and moves through
    # all of the preceding events until it gets to Start
    def getMainList(self):
        mainList = []
        event = self.HEAD
        while event.precedingEvent is not None:
            mainList.append(event)
            event = event.precedingEvent

        return mainList


# The Game event and all of its children are the specific event objects to be recorded
# as the primary data type. Note: I fail to see utility in keeping the data, but better
# to have it I suppose.

# Game event is the superclass for all other class events, for now, I may want to include
# a Program event later, we'll see
class GameEvent():
    def __init__(self):
        self.precedingEvent = None
        self.antecedingEvent = None
        self.pointsValue = 0
        self.time = None
        print("made event ", self.__class__.__name__)
##    def undo(self):
##        self.precedingEvent.antecedingEvent = self
##        return self.precedingEvent

    def setAntecedingEvent(self, event):
        self.antecedingEvent = event

    def setPrecedingEvent(self, event):
        self.precedingEvent = event

# This event should only ever be used at the start of the event list, it doesn't undo
class StartEvent(GameEvent):
    def __init__(self):
        GameEvent.__init__(self)
        self.precedingEvent = None

    def undo(self):
        #overwrites GameEvent to do nothing on undo
        pass

class Auto_MoveForwandEvent(GameEvent):
     def __init__(self, success=True):#success may not apply
        GameEvent.__init__(self)
        self.success = success
        if success:
            self.pointsValue = 5


class Auto_HighGoalEvent(GameEvent):
    def __init__(self, success, hot=False):
        self.hot = hot
        GameEvent.__init__(self)
        self.success = success
        if success:
            self.pointsValue = 15
            if hot is True:
                self.pointsValue += 5

class Auto_LowGoalEvent(GameEvent):
    def __init__(self, success, hot=False):
        self.hot = hot
        GameEvent.__init__(self)
        self.success = success
        if success:
            self.pointsValue = 6
            if hot is True:
                self.pointsValue += 5

#Was going to use this class as a super for H/L Goal and Auto H/L goal, but too complex
##class GoalEvent(GameEvent):
##    def __init__(self, auto=False, hot=False):
##        GameEvent.__init__(self)
##        self.autonomous = auto
##        if self.autonomous is False:
##            self.hot = False
##        else:
##            self.hot = hot
##
##        self.pointsValue = 10
##
##        if self.autonomous is True:
##            self.pointsValue += 5
##        if self.hot is True:
##            self.pointsValue += 5

class HighGoalEvent(GameEvent):
    def __init__(self, success):
        GameEvent.__init__(self)
        self.success = success
        if success:
            self.pointsValue = 10

class LowGoalEvent(GameEvent):
    def __init__(self, success):
        GameEvent.__init__(self)
        self.success = success
        if success:
            self.pointsValue = 1

# Dummy classes for potential future event
class TrussThrowEvent(GameEvent):
    def __init__(self, success):
        GameEvent.__init__(self)
        self.success = success
        if success:
            self.pointsValue = 10


class TrussCatchEvent(GameEvent):
    def __init__(self, success):
        GameEvent.__init__(self)
        self.success = success
        if success:
            self.pointsValue = 10
    
class AssistPassEvent(GameEvent):#does not record points
    def __init__(self, success):
        GameEvent.__init__(self)
        self.success = success
        
    
class AssistRecieveEvent(GameEvent):#does not record points
    def __init__(self, success):
        GameEvent.__init__(self)
        self.success = success
        
    
class Comment():
    def __init__(self,title, description="",ranking=None):
        self.title = title
        self.description=description
        self.ranking = ranking
        
class pitScout():
    def __init__():
        pass
    
