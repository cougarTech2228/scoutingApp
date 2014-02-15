# user interface module


import cmd
import sys


class Com(cmd.Cmd): #global commands

    def __init__(self, main, lock):
        cmd.Cmd.__init__(self)
        self.lock = lock #unused as of yet, may be needed for later issueswith threading
        self.lock.acquire()        
        self.main = main
        self.prompt = '>>>>>'
        self.state = self.main.state
        self.triedCommand = []
        self.lock.release()
        while self.state.instartup:
            pass
        


    '''
    def do_failed_message(self):
        time.sleep(.5)
        if self.glob:
            if len(triedCommmand) == 5:#each command object could not process it
                for s in self.triedCommand:
                    if(s[1:] == s[:-1]):# no idea how this works but should check if all list elements are equal (according to the internet)
                        print("sorry, ", self.triedCommand, " is not a valid command in this mode")
                        print("please refer to help for command information")

        else:
            pass
    '''
            
    #put global commands here
    
    #format
    '''
    def do_command(self, t): i have no idea what it s returning for t (maybe arguments)
    ''' 
    def do_matchMode(self, t):
        self.state.enterMatchMode()

    def do_quit(self, t):
        if confirm(m = "quit (y/n)"):   
            self.state.exit = True
            sys.exit(1)
        else:
            pass
        

    def help_quit(self, t):
        print("syntax: quit")
        print("-- terminates the application")


    #match commands----------------------------------------------------------

    # shortcuts
    do_q = do_quit
     
    def do_p(self, t):
        if self.state.matchRunning:
            self.state.togglePause()
        else:
            print("you cant toggle pause,no match is running")
            
    def do_pause(self, t):
        if self.state.matchRunning:
            self.state.pauseSet(True)
        else:
            print("you can't pause,no match is running")
            
    def do_start(self, t):
        if self.state.matchReadyStart:
            self.state.startMatch()
            print("match started")
        else: 
            print("you can't start a match now")
            self.do_gets(t)
    def do_end(self, t):
        if self.state.matchRunning:
            self.state.endMatch()
        else:
            print ("you can't end a match: no match running")
        
    def do_restart(self, t):
        if self.state.matchMode:
            if confirm():
                self.state.resetMatch(self)   
        else:
            print("no match to reset")
    
    #setupcommands-----------------------------------------------------------
    
    def do_stm(self, t):
        self.state.inSetup =True
        setupmatch(self.main)
       
    def do_gets(self, t):
        for i in self.state.getState():
            print(i[1],i[0])
            
    def do_echon(self, t):
        self.state.echo = not self.state.echo
                
class Test(cmd.Cmd):
    
    def __init__(self, main):
        cmd.Cmd.__init__(self)
        self.main = main
            
    def do_testing(self, t):# t stands for random thing i dont know what it is
        print("hello")

    def do_gets(self, t):
        print(self.main.state.matchPaused)
        self.main.state.togglePause()
        print(self.main.state.matchPaused)

def init(m):
    Com(m, m.lock).cmdloop()
    #Test(m).cmdloop()


   
def strcIn(allowed = None, message = "", typeInt = False, check = False):
    while True:
        re = input(message)
        if allowed:
                if re not in allowed:
                    print("that is not a valid answer")
                    continue
        if typeInt:
            try:
                v = int(re)
                re = v
            except (ValueError):
                print("that is not a valid answer")
                continue
                
        if check == True:
            if not confirm(re):
                continue
            
        return re
    

def confirm(m = "is this okay - y/n"):
    print (m)
    a = strcIn(allowed = ["n","y","Y","N","yes","no","Yes","No"], message = "y/n-->>")
    if a in ["y","Y","yes","Yes"]:
        return True
    else:
        return False
        
        
        
def setupmatch(main, match=None):
    if match:   
        pass
    elif main.state.currentMatch:
        match = main.state.currentMatch.number + 1
    elif main.state.lastMatch:
        match = main.state.lastMatch.number + 1
    else:
        match = 1
    print("set-up next match: #", match, "? ")
    if not confirm():
        match = main.data.getUndefinedMatch()
        print("setup next undefined match: #",match,"?" )
        if not confirm():
            print ("what match to set-up: (number)")
            num = strcIn(typeInt = True, message = "match number>>")
            match = num
    
    def getRobots():# can this be done
        robots = []
        #enter red alliance
        robots.append(strcIn(typeInt = True, message ="Red alliance robot 1->>"))
        robots.append(strcIn(typeInt = True, message ="Red alliance robot 2->>"))
        robots.append(strcIn(typeInt = True, message ="Red alliance robot 3->>"))
        
        #enter blue alliance
        robots.append(strcIn(typeInt = True, message ="Blue alliance robot 1->>"))
        robots.append(strcIn(typeInt = True, message ="Blue alliance robot 2->>"))
        robots.append(strcIn(typeInt = True, message ="Blue alliance robot 3->>"))
        return robots
        
    c = False   
    while not c:
        robos=[]
        robos = getRobots()
        c = confirm()
        
    while True:
        print("commit or escape")
        re = strcIn(message = ">>>>")
        if re == "commit":
            main.data.matchCreate(robos, match)
            return True
            
        elif re == "escape" or re == "E":
            print("aborting setup match")
            return False#leave function
            
        
            
def prepareMatch(main):
    if main.state.matchMode:
        print("you cant prepare for next math in match")
    if main.state.lastMatch:
        match = main.state.lastMatch.number+1
    else:
        match = 1
    
    print ("prepare next match: #",match," ?")
    if not confirm:
        match = strcIn(m="what match to prepare:",typeInt=True,check=True )
        
    try:
        main.data.competition[match-1]
        
    except:
        print("you cant prepare a undefined match, would you like to set it up now?")
        if confirm():
            if not setupmatch(main,match=match):
                print("aborting prepare match")
                return
                
        while True:
            c = False
            while not c:
                for r in main.data.competition[match-1].robots:
                    print("press button one on joyStick for robot:",r.teamNumber)
                    inputOb = main.Joy.getJoy()
                c = confirm()
                