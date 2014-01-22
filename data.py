# Database module #merged some modules

class CompetitianList(list):
    def __init__():
        pass

    def addComp(self, name):
        self.append(Competition(name))


class Competition(list):

    def __init__(self, numberOfMatches=0, name="Test"):
        # If numMatches = 0 then number of matches in competician is unknown
        # name is a name given for this competitian ex) 'FLR seeding', 'FLR
        # final', 'nationals Finals'
        self.name = name
        #self.current_match = 0
        #self.last_match = 0
        self.numMatches = numberOfMatches

    def newMatch(self, teamNumbers, place = None):
        # New Match takes a list of robot numbers as an argument
        ##self[0] += 1
        #self.last_match += 1
        self.inMatches=len(self)+1
        #inmatches is the # of inputed matches
        if place is None:
            self.append(Match(self.inMatches, robots, self.name))
        else:
            self.insert(place, Match(self.inMatches, robots, self.name))
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
        n = 0
        for teamNumber in teamNumbers:
            # This will create a new robot each time it is called

            robots[n] = InMatchRobot(teamNumber,self, n, self.comp)
            n += 1  # [0:2] red, [3:5] blue
            pass


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




class InMatchRobotRecords:
    def __init__(self, compName, myMatch, robot, ally):
        self.comp = compName #compatician name
        self.match = myMatch #match object
        self.roboNum = robot #robot number
        self.alliance = ally # string (RED or BLUE)
        self.events = GameEventList() #is this right, this class could possibly extend game evt list
        self.comments = []
        # variables being recorded ex)shots missed, points scored, climberlevel reached

    def addEvt(event):
        pass
        #add event to event list

    def tally():
    #tally up evt list
        pass


#---------------------------------------------------------------------------------


#Stored data
# Database module

#from events import *
# forgive me but it was driving me crazy with the events objects in this module,
# probably the opposite of your feeling (this line should take care of any issues right)


class RobotList(list):
    """This class inherits from the list class, it will handle all robot objects"""
    def __init__(self):
        self.current_robot_index = 0
        self.robotKeys = []
        self.current_robot = None

    def __str__(self):
        return str([robot.teamNumber for robot in self])


    def add(self, robot):
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
        self.current_robot = robot
        self.current_robot_index = self.index(robot)

        return True


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

    def removeTeamNumber(self, teamNumber):
        # Removes a robot based on it's number
        robotVar = self.getRobot(teamNumber)
        self.removeRobot(robotVar)

    def setCurrentRobot(self, teamNumber):
        self.current_robot = self[self.robotKeys.index(teamNumber)]
        self.current_robot_index = self.index(robot)


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



class Robot():
    def __init__(self, teamNumber):
        self.teamNumber = teamNumber
        self.matches = []
        self.totalPts = 0
        # has robo record files
        #self.__deleted = False

    def addMatch(self, records):
        self.matches.append(records)

    def calculateStats(self):
        self.totalPts = 0
        for record in self.matches:
            for event in record:
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

class Auto_HighGoalEvent(GameEvent):
    def __init__(self, hot=False):
        self.hot = hot
        GameEvent.__init__(self)
        self.pointsValue = 15
        if hot is True:
            self.pointsValue += 5

class Auto_LowGoalEvent(GameEvent):
    def __init__(self, hot=False):
        self.hot = hot
        GameEvent.__init__(self)
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

    def __init__(self):
        GameEvent.__init__(self)
        self.pointsValue = 10

class LowGoalEvent(GameEvent):
    def __init__(self):
        GameEvent.__init__(self)
        self.pointsValue = 1

# Dummy classes for potential future event
class TrussThrowEvent(GameEvent):
    pass

class BallCatchEvent(GameEvent):
    pass
