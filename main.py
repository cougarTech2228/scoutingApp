# Main module

# As of this build main.py is inoperational.
# To test the program, open test.py or run main_test.py
import user
import joy
import data
import threading
import pygame
import sys
import time

class Main():
    def __init__(self):
        pygame.init()
        pygame.event.set_grab(False)
        
    def start(self, delay = True):
        if delay:
            #added delays so it will look cooler when loading
            print ("program loading")
            time.sleep(1)
            self.state = State()
            print("initiated program state")
            time.sleep(.2)
            self.inputs = joy.joystick_init(test = True)
            print("joysticks initialised")
            time.sleep(.2)
            self.data = Data(self)
            print("created data structure ")
            time.sleep(.2)
            print("working ")
            time.sleep(1)
            self.lock = threading.Lock()
            self._comThread = threading.Thread(target = user.init, args = (self,))
            self._joyThread = threading.Thread(target = joy.run, args = (self.state, self.lock))
            self._joyThread.start()
            print("scouter input listener initialised ")
            self._comThread.start()
            time.sleep(.1)
            print("user input object created")
            time.sleep(1)
            self.state.instartup = False
            print("\nprogram running")
            '''
            q = False
            while not q:
                com.cmdGo()
                joy.check(self.state)
                print ("loop")
            '''
            while not self.state.exit:
                pass
            
            print("program closing")
            time.sleep(1)
            sys.exit(1)
        else:
            #added delays so it will look cooler when loading
            print ("program loading")
            self.state = State()
            print("initiated program state")
            self.inputs = joy.joystick_init(test = True)
            print("joysticks initialised")
            self.data = Data(self)
            print("created data structure ")
            print("working ")
            self.lock = threading.Lock()
            self._comThread = threading.Thread(target = user.init, args = (self,))
            self._joyThread = threading.Thread(target = joy.run, args = (self.state, self.lock))
            self._joyThread.start()
            print("scouter input listener initialised ")
            self._comThread.start()
            print("user input object created")
            self.state.instartup = False
            print("\nprogram running")
            '''
            q = False
            while not q:
                com.cmdGo()
                joy.check(self.state)
                print ("loop")
            '''
            while not self.state.exit:
                pass
            print("program closing")
            sys.exit(1)
                
        
class Data(): 
    def __init__(self, main): #reminder -this must be fixed
        self.competition = data.Competition()
        self.main = main
        self.robots = data.RobotList()
    
#       self.state.currentComp = self.competitionList[-1]  #This isn't going to work, the list is empty
#       self.state.currentMatch = self.compList[-1][-1]
        
        self.temp_records  = [ i for i in range(len(self.main.inputs))]
        self.matchEvtList = None #evt list

    def matchCreate (self, robots, placement=None):
        if placement is None:
            self.competition.newMatch(robots)
            
        else:
            self.competition.newMatch(robots, placement)
           
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
            self.robotList.addRobot(data.Robot(teamNumber.strip()))
            
    def gameEvtRecord(self, joy, evt):
    # record correct bot and evt
        self.temp_records[joy].addEvt(evt)
        self.matchEvtList.add(evt) #add evt

    def commitMatch(self):
        for i in self.temp_records:
            i.tally
            for r in self.state.currentMatch.robots:
                if r.name == i.name:
                    r.records = i
        self.state.currentMatch.events = self.matchEvtList

    def save(self):
        import pickle
        save_file = open(self.theCompetition.name + ".dat", "wb")
        save_data = [self.theCompetition,self.robotList ]
        
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
        self.echo = False
        self.exit = False
        self.reset()
        self.instartup = True
    def getState(self):
        self.stlr()
        return self.statelist

    def reset(self):
        self.statelist = []      
        self.inMatch = False
        self.inSetup = False
        self.inReview = False
        self.inTest = False
        self.matchReadyStart = False
        self.matchReadyCommit = False
        self.matchPaused = False
        self.matchEnded = False
        self.matchRunning = False
        self.currentMatch = None #only defined in match
        self.lastMatch = None #previous match
        
        
    def stlr(self):#state list reset
        self.statelist = []      
        self.statelist.append( [self.inMatch, "inMatch"])
        self.statelist.append( [self.inSetup,"inSetup"])
        self.statelist.append( [self.inReview,"inReview"])
        self.statelist.append( [self.inTest ,"inTest"])
        self.statelist.append( [self.matchReadyStart,"matchReadyStart"])
        self.statelist.append( [self.matchReadyCommit,"matchReadyCommit"])
        self.statelist.append( [self.matchPaused,"matchPaused"])
        self.statelist.append( [self.matchEnded,"matchEnded"])
        self.statelist.append( [self.matchRunning ,"matchRunning"])
        self.statelist.append( [self.currentMatch,"currentMatch"])
        self.statelist.append( [self.lastMatch,"lastMatch"])
        
    def enterMatchMode(self):
        self.inMatch = True
        self.matchReadyStart = True
        self.matchPaused = True
        if self.echo:
            print("entering match mode")      
        
    def togglePause(self):
        self.matchPaused = not self.matchPaused
        if self.echo:
            print("pause", self.matchPaused)
            
    def pauseSet(self, set):
        self.matchPaused = set
        if self.echo:
            print("pause", self.matchPaused)
        
    def startMatch(self):
        self.matchPaused = False
        self.matchReadyStart = False
        self.matchRunning = True
        self.matchEnded = False
        self.matchReadyCommit = False
        if self.echo:
            print("match started")    
            
    def endMatch(self):
        self.matchReadyStart = False
        self.matchReadyCommit = True
        self.matchPaused = False
        self.matchEnded = True
        self.matchRunning = False
        if self.echo:
            print("match ended")        
        
    def resetMatch(self):
        data.resetMatch()
        self.matchReadyStart = True
        self.matchReadyCommit = False
        self.matchPaused = True
        self.matchEnded = False
        self.matchRunning = False
        if self.echo:
            print("match reset")      
        
    def exitMatchMode(self):
        self.inMatch = False
        self.matchReadyStart = False
        self.matchReadyCommit = False
        self.matchPaused = False
        self.matchEnded = False
        self.matchRunning = False
        self.lastMatch = self.currentMatch
        self.currentMatch = None
        if self.echo:
            print("leaving match mode")              
        
    def enterSetupMode(self):
        self.inSetup = True

        
    def setMatch(self, match, comp = None):
        if comp:
            self.currentComp = self.main.dataMain.compList.getComp(comp)
            pass
        self.currentMatch = self.currentComp[match-1]
        
        
        
if __name__ == "__main__": #This part is so that when it is imported, the following code doesn't run   
    main = Main()
    main.start()




