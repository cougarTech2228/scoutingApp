# Test run for the Main module5

import user
import joy
import data
import threading

class Main():
    def __init__(self):
        self.inputs = joy.joystick_init(True)
        self.data = Data(self.inputs)
        user.do_init()
        self.state = State()

    def set_up(self):
        pass
       
    def enterMatchMode(self):
        self.state.inMatch = True
        self.state.matchReadyStart = True
        self.state.inMatch = True
        self.state.inMatch = True
        joy.pause = True
        joy.end = False
        t = threading.thread(target = joy.run)
        t.start()
        
class Data(): 
    def __init__(self, inputs): #reminder -this must be fixed
        self.compList = data.CompetitionList(test = True)
        self.Robots = data.RobotList()
        self.currentComp = self.compList[-1]
#        self.currentMatch = self.compList[-1][-1] #When you start the program you havent entered matches
        self.temp_records  = []
        self.matchEvtList = None #evt list
        for i in inputs:
            self.temp_records.append(i) #can this be done

    def matchCreate(robots, placement=None):
        if placement is None:
            self.currentComp.newMatch(robots)
            
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
            i.tally
            for r in self.currentRobots:
                pass
        if r.name == i.name:
                    r.records = i
        self.currentMatch.events = self.matchEvtList
        

    
    #this will now need to find the correct robot objects and append a inmatch robot records to its match list

class State():
    def __init__(self):
        self.reset()

    # This function is less than pointless, it has some sort of weird inverted point
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

    


if __name__ == "__main__": #This part is so that when it is imported, the following code doesn't run   
    main = Main()
    main.set_up()



