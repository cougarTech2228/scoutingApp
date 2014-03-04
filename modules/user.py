# user interface module


import cmd
import sys
import os
from main import NUMBERROBOTSPERMATCH 


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
        if self.state.nextMatch:
            self.state.enterMatchMode()
        else:
            print("must first prepare match")
            
    def help_matchMode(self):
        print("syntax: matchMode")
        print("Puts the program into a state such that it can start the match")
            
    def do_quit(self, t):
        if confirm(m = "quit (y/n)"):   
            self.state.exit = True
            sys.exit(1)
        else:
            pass
        
    def help_quit(self):
        print("syntax: quit")
        print("shortcut: q")
        print("-- terminates the application")
        
    def do_preMatch(self,t):    
        prepareMatch(self.main)
        
    def help_preMatch(self):
        print("syntax: preMatch")
        print("shortcut: pfm")
        print("""Enter the prematch setup, it defaults to prepare for a new match \r
                indexed after the last match in the registry.  If no match is set up \r
                the program enters setup match""")

    def do_autoEnd(self, t):
        if "on" in t:
            self.main.state.autoEndMatch = True
            print ("automatically end matches is on")
        elif "off" in t:
            self.main.state.autoEndMatch = False
            print ("automatically end matches is off")
            
        else:
            print('"',t,'" is not a valid command')
            print("try 'autoEnd off' or 'autoEnd on'")
            
    def help_autoEnd(self):
        print("syntax: autoEnd <on/off>")
        print("""Sets the state of autoEnd, if autoEnd is set to on the match \r
                will end automatically in the set time, when set to off the user \r
                will have to end the program manually""")
    #match commands----------------------------------------------------------

    # shortcuts
    do_q = do_quit
    help_q = help_quit
     
    def do_pause(self, t):
        if self.state.matchRunning:
            self.state.togglePause()
        else:
            print("you cant toggle pause,no match is running")
            
    do_p = do_pause
    
    def help_pause(self):
        print("syntax: pause")
        print("shortcut: p")
        print("Pauses the game is the game is running, unpauses if paused")
        
    help_p = help_pause
            
    def do_start(self, t):
        if self.state.matchReadyStart:
            self.state.startMatch()
        else: 
            print("you can't start a match now")
            self.do_gets(t)
            
    def help_start(self):
        print("""When a match is setup, prepared and matchMode has been activated, \r
              this command starts the match""")
            
    def do_commit(self,t):
        if self.state.matchReadyCommit:                
            if confirm():
                self.main.data.commitMatch()
                
    def help_commit(self):
        print("Confirms a choice when prompted to commit")
            
    def do_end(self, t):
        if self.state.matchRunning:
            self.state.endMatch()
        else:
            print ("you can't end a match: no match running")
            
    def help_end(self):
        print("syntax: end")
        print("-- ends the match when a match is running")
        
    def do_restart(self, t):
        if self.state.matchMode:
            if confirm():
                self.state.resetMatch(self)   
        else:
            print("no match to reset")
            
    def help_restart(self):
        print("syntax: restart")
        print("Starts a match over again if there is a match running")
            
    def do_esc(self, t):
        if self.state.matchMode:
            self.main.state.exitMatchMode()
            
    def help_esc(self):
        print("syntax: esc")
        print("When a match is running, this command exits the match")
    
    #setupcommands-----------------------------------------------------------
    
    def do_setupMatch(self, t):
        self.state.inSetup =True
        setupmatch(self.main)
       
    def do_gets(self, t):
        for i in self.state.getState():
            print(i[1],i[0])
            
    def do_echon(self, t):
        self.state.echo = not self.state.echo
        
    def do_review(self, t):
        if "-i" in t:
            try:
                import review.py

            except StopIteration:
                pass
        else:    
            os.system('./REVIEW.sh')
    
    def do_show(self, t):
        if "ds" in t:
            for m in self.main.data.competition:
                if m:
                    print("match ",m.number)
                    for r in m.robots:
                        print("    team ", r.teamNumber)
                        
        else:
            print("show needs a parameter")
                        
    def do_save(self, t):
        self.main.data.save()
        
    def help_save(self):
        print("syntax: save")
        print("shortcut: s")
        print("saves the game data to  <competition_name>.dat in ./resources/save_files")
                
                
    do_stm = do_setupMatch
    do_pfm = do_preMatch
<<<<<<< HEAD
    do_s = do_save 
=======
    help_pfm = help_preMatch
    do_s = do_save
    help_s = help_save
>>>>>>> 4b5ae30cbbaa8a160b325cf74ec2e382be9f1f54
    
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
    

def confirm(m = "is this okay", safe = True):
    print (m)
    if safe:
        a = strcIn(allowed = ["n","y","Y","N","yes","no","Yes","No"], message = "y/n-->>")
        if a in ["y","Y","yes","Yes"]:
            return True
        else:
            return False
    else:
        a = strcIn(allowed = ["n","y","Y","N","yes","no","Yes","No", ""], message = "y/n-->>")
        if a in ["y","Y","yes","Yes"]:
            return True
        elif a == "":
            return True
        else: 
            return False
        
        
def setupmatch(main, match=None, nor = NUMBERROBOTSPERMATCH): #nor  = number of robots per alliance
    f = False
    
    if match:
        print("setting up match")
    
    else:
        match = main.data.getUndefinedMatch()
        print("setup next undefined match: #",match,"?" )
        if not confirm():
            
            if main.state.currentMatch:
                match = main.state.currentMatch.number + 1
            elif main.state.lastMatch:
                match = main.state.lastMatch.number + 1
            else:
                match = 1
                
            print("set-up next match: #", match, "? ")
            if not confirm():
                print ("what match to set-up: (number)")
                num = strcIn(typeInt=True, message="match number>>")
                match = num
                try:
                    if main.state.currentMatch.number == match:
                        print("you cant setup that match, you are already in it")
                        return False
                except:
                    pass
                
    try:
       if main.data.competition[match-1]:
            print("match already exists, would you like to override it.\n (this could be a destructive process)")
            if not confirm():
                return False
            else:
                f = True#must force override of match
    except:
        pass
            
    def getRobots(num):# can this be done
        robots = []
        #enter red alliance
        for color in ("RED","BLUE"):
            for n in range(num):
                string = color + " alliance robot #" + str(n+1) + " >>>"
                robots.append(strcIn(typeInt = True, message = string))
            
        return robots
        
    c = False   
    while not c:
        robos=[]
        robos = getRobots(nor)
        c = confirm()
        
    while True:
        print("commit or escape")
        re = strcIn(message = ">>>>")
        if re == "commit":
            main.data.matchCreate(robos, match, f)
            return True
            
        elif re == "escape" or re == "E":
            print("aborting setup match")
            return False#leave function
            
        
            
def prepareMatch(main):
    if main.state.inMatch:
        print("you cant prepare for next math in match")
        return
    elif main.state.nextMatch:
        match = main.state.nextMatch
        print("Match already prepared. Would you like to continue?")
        if not confirm():
            return
    elif main.state.lastMatch:
        match = main.state.lastMatch.number+1
    else:
        match = 1
        
    print ("prepare next match: #",match," ?")
    if not confirm():
        match = strcIn(message="what match to prepare:",typeInt=True,check=True )
        print ("prepare match ", match)        
        
    try:
        main.data.competition[match-1]
        
    except:
        print("you cant prepare a undefined match, would you like to set it up now?")
        if confirm():
            if not setupmatch(main,match=match):
                print("aborting prepare match")
                return
        else:
            print("aborting prepare match")
            return
                
    c = False
    while not c:
        port=0
        for robot in main.data.competition[match-1].robots:
            print("press button one on joyStick for robot:",robot.teamNumber)
            inputOb = main.Joy.getJoy()#returns id
            main.data.setPort(port,robot)
            main.connect.setPorting(inputOb, port)                
            port+=1
        c = confirm()
            
    main.state.nextMatch = main.data.competition[match-1]
        
       
