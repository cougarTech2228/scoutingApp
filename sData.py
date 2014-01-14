#Stored data
# Database module

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

class Robot():
    def __init__(self, teamNumber):
        self.teamNumber = teamNumber

# The Game Event List is the log of all events that the user inputs, since each
# Game event objecct points to the one before it, there is no need to order it.
# That is, each event can simply be added to the end of the list
class GameEventList(list):
    def __init__(self):
        self.eventIndexCounter = -1
        self.HEAD = None
        self.add(StartEvent())
        
        self.HEAD = self[-1]

    def add(self, event):
        self.append(event)
        # Have the old event point to the added event
        # and the new event point to the preceding event
        self.HEAD.setAntecedingEvent(event)
        event.setPrecedingEvent(self.HEAD)
        self.eventIndexCounter += 1
        self.HEAD = self[self.eventIndexCounter]
        

    def undo(self):
        if self.HEAD.predecingEvent is not None:
            self.HEAD = self.HEAD.precedingEvent

    def redo(self):
        if self.HEAD.antecedingEvent is not None:
            self.HEAD = self.HEAD.antecedingEvent

    # getMainList returns a list starting at head, and moves through
    # all of the preceding events until it gets to Start
    def getMainList(self):
        mainList = []
        event = self.HEAD
        while pre_event is not None:
            mainList.append(event)
            event = event.precedingEvent


# The Game event and all of its children are the specific event objects to be recorded
# as the primary data type. Note: I fail to see utility in keeping the data, but better
# to have it I suppose.

# Game event is the superclass for all other class events, for now, I may want to include
# a Program event later, we'll se
class GameEvent():
    def __init__(self, precedingEvent=None):
        self.precedingEvent = precedingEvent
        self.antecedingEvent = None
        self.pointsValue = 0

    def undo(self):
        self.precedingEvent.antecedingEvent = self
        return self.precedingEvent

    def setAntecedingEvent(self, event):
        self.antecedingEvent = event

    def setPrecedingEvent(self, event):
        self.precedingEvent = event

class StartEvent(GameEvent):
    def __init__(self):
        GameEvent.__init__(self)
        self.precedingEvent = None

    def undo(self):
        #overwrites GameEvent to do nothing on undo
        GameEvent.undo(self)
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

class TrussThrowEvent(GameEvent):
    pass

class BallCatchEvent(GameEvent):
    pass


class RobotMatchPerformacne():
    def __init__(self, teamNumber, myMatch, num):
        # I don't know what comp does, and it isn't used in the program
        pass
                        
class RobotRecords:
    def __init__(self, comp, myMatch, robot, alliance):
        pass
        # variables being recorded ex)shots missed, points scored, climberlevel reached


