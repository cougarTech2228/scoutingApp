# The Game event and all of its children are the specific event objects to be recorded
# as the primary data type. Note: I fail to see utility in keeping the data, but better
# to have it I suppose.

# Game event is the superclass for all other class events, for now, I may want to include
# a Program event later, we'll se
class GameEvent():
    def __init__(self):
        self.precedingEvent = None
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


