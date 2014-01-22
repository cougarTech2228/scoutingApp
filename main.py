# Main module

# As of this build main.py is inoperational.
# To test the program, open test.py or run sData_test.py
import user
import joy
import data
import threading

class Main():
    def __init__(self):
        self.inputs = joy.joystick_init()
		self.data = Data(len(inputs))
        user.init()
		self.state = State()
        pass
	   
	def enterMatchMode:
        self.state.inMatch = True
        self.state.matchReadyStart = True
        self.state.inMatch = True
        self.state.inMatch = True
        joy.pause = True
        joy.end = False
        t = threading.thread(target = joy.run)
        t.start()
        
class Data(): 
    def __init__(self, numInputs): #reminder -this must be fixed
        self.compList = data.CompetitianList()
        self.Robots = data.RobotList()
		self.state.currentComp = self.compList[-1]
		self.state.currentMatch = self.compList[-1][-1]
		self.temp_records  = []
		self.matchEvtList = #evt list
        for i in range(numInputs):
            self.temp_records.append(None) #can this be done
        pass

	def matchCreate(robots, placement=None):
        if placement=None:
            self.currentComp.newMatch(robots):
            
        else:
            self.currentComp.newMatch(robots, placement)
            
    def setRobots(self, joy, robot): #set robots for match with inputs
        self.temp_records[joy] = data.InMatchRobotRecords(robot.myMatch.comp.name, robot.myMatch.matchNum, robot.alliance)

    def gameEvtRecord(self, joy, evt):
	# record correct bot and evt
		self.temp_records[joy].addEvt(evt)
		self.matchEvtList.add(evt) #add evt

    def commitMatch(self):
        for i in temp_records:
            i.tally:
            for r in self.currentRobots:
		if r.name == i.name:
                    r.records = i
		self.currentMatch.events = self.matchEvtList
        

	
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
        self.currentComp = None
        self.currentMatch = None

	


	
main = Main()
main.set_up()



