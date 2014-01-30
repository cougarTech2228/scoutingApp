# Main module

# As of this build main.py is inoperational.
# To test the program, open test.py or run main_test.py
import user
import joy
import data
import threading

class Main():
    def __init__(self):
        self.state = State()
        self.inputs = joy.joystick_init()
        self.data = Data(self)
        user.init()      
        
class Data(): 
    def __init__(self, main): #reminder -this must be fixed
        self.competition = data.Competition()
        self.main = main
        self.robots = data.RobotList()

#        self.state.currentComp = self.competitionList[-1]  #This isn't going to work, the list is empty
#        self.state.currentMatch = self.compList[-1][-1]
        
        self.temp_records  = [ i for i in len(main.inputs)]
        self.matchEvtList = None #evt list

    def matchCreate(robots, placement=None):
        if placement is None:
            self.state.currentComp.newMatch(robots)
            
        else:
            self.state.currentComp.newMatch(robots, placement)
           
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
        self.temp_records[joy] = data.InMatchRobotRecords(robot.myMatch.comp.name, robot.myMatch.matchNum, robot.alliance)

    def add_robots_from_file(self, fileName="robots_test.txt"):
        file = open(fileName).readlines()
        for teamNumber in file:
            self.robotList.addRobot(Robot(teamNumber.strip()))
            
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

    def save(self):
        import pickle
        save_file = open(self.theCompetition.name + ".dat", "wb")
        save_data = [self.theCompetition,
                     self.robotList ]
        
        pickle.dump( save_data, save_file )
        save_file.close()

    def load(self, fileName):
        import pickle
        load_data = pickle.load( open(fileName, "rb") )
        self.theCompetition = load_data[0]
        self.robotList = load_data[1]
        
    def matchReset(self):
        pass
'''
    def setMatch(self, match, comp = None):
        if comp:
            #must searth for comp
            pass
'''           
    

class State():
    def __init__(self): #, myMain):
#        self.main = myMain
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
        self.matchEnded = False
        self.matchRunning = False
        
        self.currentComp = None
        self.currentMatch = None
        self.lastMatch = None
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
            
    def pauseSet(set):
        self.matchPaused = set
        
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
        self.lastMatch = self.currentMatch
        self.currentMatch = None
        
        
    def enterSetup(self):
        self.inSetup = True

        
    def setMatch(self, match, comp = None):
        if comp:
            self.currentComp = self.main.dataMain.compList.getComp(comp)
            pass
        self.currentMatch = currentComp[match-1]
        
        
if __name__ == "__main__": #This part is so that when it is imported, the following code doesn't run   
    main = Main()
    main.set_up()



