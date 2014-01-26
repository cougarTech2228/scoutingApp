# Test run for the Main module5

import user
import joy
import data
import threading

class Main():
    def __init__(self):
        self.state = State()
        self.inputs = joy.joystick_init(True)
        self.data = Data(self)
        user.do_init()
        
"""
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
"""

class Data(): 
    def __init__(self, main):
        self.theCompetition = data.Competition("Test")
        self.robotList = data.RobotList()
        self.add_robots_from_file()

        self.main = main
        self.temp_records  = [i for i in main.inputs]
        self.matchEvtList = None #evt list

    def matchCreate(robots, placement=None):
        if placement is None:
            self.currentComp.newMatch(robots)
            
        else:
            self.currentComp.newMatch(robots, placement)

    def add_matches_from_file(self, fileName="matches.txt"):
        file = open(fileName, "r")
        for line in file:

            eol = False #end of line
            firstWord = True
            matchNum = 0
            robotNums = []
            
            if line[0] == "#":
                ##print("pass")
                eol = True    
            
            while not eol:
                word = ""
                for letter in line:
                    
                    if letter == " " or letter == "\t": #a space or tab
                        if firstWord is True:
                            matchNum = int(word)
                            ##print("Match Number: " + word)
                            firstWord = False
                            word = ""
                        else:
                            robotNums.append(int(word))
                            ##print("Robot Number: " + word)
                            word = ""
                            
                    elif letter == "\n" or letter == "\r":
                        eol = True
                        
                    else:
                        word += letter
                        
            if matchNum != 0:
                self.competition.newMatch(robotNums, matchNum)
            
    def setRobots(self, joy, robot): #set robots for match with inputs
        self.temp_records[joy] = data.InMatchRobotRecords(robot.myMatch.comp.name,
                                                          robot.myMatch.matchNum,
                                                          robot.alliance)

    def add_robots_from_file(self, fileName="robots_test.txt"):
        file = open(fileName).readlines()
        for teamNumber in file:
            self.robotList.add(data.Robot(teamNumber.strip()))

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

    def matchReset(self):
        pass
        

    
    #this will now need to find the correct robot objects and append a inmatch robot records to its match list

class State():
    def __init__(self):
        self.reset()
        
##    def getState(self):
##        return self

    def reset(self):
        self.inMatch = False
        self.inSetup = False
        self.inReview = False
        self.inTest = False

        self.matchReadyStart = False
        self.matchReadyCommit = False
        self.matchPaused = False
        self.matchEnded = False
        self.matchRunning = False
        
        self.currentComp = None
        self.currentMatch = None
        
        #self.matchIsSetup = False
        
        
    def enterMatchMode(self):
        self.inMatch = True
        self.matchReadyStart = True
        
        self.matchPaused = True
        joy.end = False
        self.t = threading.thread(target = joy.run(self.matchPaused, self.matchEnded))
        self.t.start()
        
    def togglePause(self):
        if self.matchPaused == True:
            self.matchPaused = False
        else:
            self.matchPaused = True
            
    def pauseSet(self):
        self.matchPaused = self
        
    def startMatch(self):
        self.matchPaused == False
        self.matchReadyStart = False
        self.matchRunning = True
        self.matchEnded = False
        self.matchReadyCommit = False
        
    def endMatch(self):
        self.matchReadyStart = False
        self.matchReadyCommit = True
        self.matchPaused = False
        self.matchEnded = True
        self.matchRunning = False
        pass
        
    def resetMatch(self):
        data.resetMatch()
        self.matchReadyStart = True
        self.matchReadyCommit = False
        self.matchPaused = True
        self.matchEnded = False
        self.matchRunning = False
        pass
        
    def exitMatchMode(self):
        self.inMatch = False
        
        self.matchReadyStart = False
        self.matchReadyCommit = False
        self.matchPaused = False
        self.matchEnded = False
        self.matchRunning = False
        
        self.currentMatch = None
        
    def enterMatchMode(self):
        self.inSetup = True

        
    def setMatch(self, match, comp = None):
        if comp:
            self.currentComp = self.main.dataMain.compList.getComp(comp)
            pass
        self.currentMatch = currentComp[match-1]
        

if __name__ == "__main__": #This part is so that when it is imported, the following code doesn't run   
    main = Main()


