# Main module

# As of this build main.py is inoperational.
# To test the program, open test.py or run sData_test.py
import user
import joy
import data

class Main():
    def __init__(self):
        pass

    def set_up(self):
	joy.joystick_init()
	self.data = Data()
        user.com()
	self.state = State()
        pass
	
class Data(): 
    def __init__(self): #reminder -this must be fixed
        self.compList = data.CompeticianList()
        self.Robots = data.RobotList()
	currentComp = self.complist[-1]
	currentMatch = self.compList[-1][-1]
	currentRobots = currentMatch.robots #in match robots
	self.temp_records  = []
	self.matchEvtList = #evt list
        pass

    def setRobots(self, joy, robot): #set robots for match with inputs
        self.temp_records[joy] = data.InMatchRobotRecords(robot.myMatch.comp.name, robot.myMatch.matchNum, robot.alliance)
                

    def gameEvtRecord(self, joy, evt):
	# record correct bot and evt
	self.temp_records[joy].addEvt(evt)
	self.matchEvtList.#add evt

    def commitMatch(self):
        for i in temp_records:
            i.tally:
            for r in currentRobots:
		if r.name == i.name:
                    r.records = i
	currentMatch.events = matchEvtList
	
	#this will now need to find the correct robot objects and append a inmatch robot records to its match list

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



