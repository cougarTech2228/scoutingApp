# Main module

# As of this build main.py is inoperational.
# To test the program, open test.py or run sData_test.py
import user
import joy

class Main():
    def __init__(self):
        pass
    def set_up(self):
	joy.joystick_init()
	
        user.com()
	self.state = State()
        pass
	
class Data(): 
    def __init__(self): #reminder -this must be fixed
        self.CompList = CompeticianList()
        self.Robots = RobotList()
	currentMatch = self.CompList[-1][-1]
	currentRobots = currentMatch.robots #in match robots
	self.inputs  = []
		
        pass

    def setRobots(joy, robot): #robot is a string 
        for i in currentRobots:# will this work
            if i.name = robot 
		inputs[i] = robot
                

    def gameEvtRecord(joy, evt):
	# record correct bot and evt

class State():
    def __init__(self):
        reset()
    	
    def getState(self):
        return self

    def reset(self):
	self.inMatch = False
        self.inSetup = False
        self.inReview = False
	self.inTest = False

        self.matchReadyStart = False
        self.matchReadyCommit = False
        self.matchPaused = False
        self.matchStopped = False
        self.matchRunning = False
	


	
main = Main()
main.set_up()



