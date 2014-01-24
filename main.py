# Main module

# As of this build main.py is inoperational.
# To test the program, open test.py or run sData_test.py
import user
import joy
import data
import threading

class Main():
    def __init__(self):
        self.state = State()
        self.inputs = joy.joystick_init()
        self.data = Data(self, len(inputs))
        user.init()
        
       

        
        
class Data(): 
    def __init__(self,main, numInputs): #reminder -this must be fixed
        self.compList = data.CompetitianList()
        self.Robots = data.RobotList()
        
        self.state = main.state
        self.state.currentComp = self.compList[-1]
        self.state.currentMatch = self.compList[-1][-1]
        
        self.temp_records  = []
        self.matchEvtList = None #evt list
        
        for i in range(numInputs):
            self.temp_records.append(None) #can this be done
        pass

    def matchCreate(robots, placement=None):
        if placement is None:
            self.state.currentComp.newMatch(robots)
            
        else:
            self.state.currentComp.newMatch(robots, placement)
            
    def setRobots(self, joy, robot): #set robots for match with inputs
        self.temp_records[joy] = data.InMatchRobotRecords(robot.myMatch.comp.name, robot.myMatch.matchNum, robot.alliance)

    def gameEvtRecord(self, joy, evt):
    # record correct bot and evt
        self.temp_records[joy].addEvt(evt)
        self.matchEvtList.add(evt) #add evt

    def commitMatch(self):
        for i in temp_records:
            i.tally
            for r in self.state.currentMatch.robots:
                if r.name == i.name:
                    r.records = i
        self.state.currentMatch.events = self.matchEvtList
        
'''
    def setMatch(self, match, comp = None):
        if comp:
            #must searth for comp
            pass
'''           
    

class State():
    def __init__(self, ):
        self.reset()
        
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
        
        #self.matchIsSetup = False
        
        
    def enterMatchMode(self):
        self.inMatch = True
        self.matchReadyStart = True
        
        joy.pause = True
        joy.end = False
        self.t = threading.thread(target = joy.run)
        self.t.start()
        
    def togglePause(self):
        if joy.pause == True:
            joy.pause = False
        else:
            joy.pause = True
            
    def startMatch(self):
        pass
        
    def endMatch(self):
        pass
        
    def resetMatch(self):
        pass
        
    def exitMatchMode(self):
        self.inMatch = False
        
        self.matchReadyStart = False
        self.matchReadyCommit = False
        self.matchPaused = False
        self.matchStopped = False
        self.matchRunning = False
        
        joy.pause = False
        joy.end = True
        
    
        
        ''' get data from automatically gather able sources such as joy.pause and joy.end
    def refresh(self):
        self.matchPaused 
        self.matchStopped
        '''
        
if __name__ == "__main__": #This part is so that when it is imported, the following code doesn't run   
    main = Main()
    main.set_up()



