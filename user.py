# user interface module


import cmd



class Com(cmd.Cmd): #global commands

    def __init__(self, main):
        cmd.Cmd.__init__(self)
        self.main = main
        self.prompt = '> '
        self.state = self.main.state
        self.triedCommand = []

    
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
            self.main.programQuit()
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
            self.do_gets()
    def do_end(self, t):
        self.state.endMatch()
        pass
        
    def do_restart(self, t):
        self.state.resetMatch(self)
        pass
    
    #setupcommands-----------------------------------------------------------
    
    def do_stm(self, t):
        self.state.inSetup =True
        setupmatch(self.main)
       
    def do_gets(self, t):
        for i in self.state.getState():
            print(i[1],i[0])
                
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
    Com(m).cmdloop()
    t = Test(m)
    #t.cmdloop()
    
   
def strcIn(allowed = None, message = "", typeInt = False, check = False):
    w = True
    while w:
        re = input(message)
        w = False
        if allowed:
                if re not in allowed:
                    print("that is not a valid answer")
                    w = True
        if typeInt:
            try:
                v = int(re)
                re = v
            except (ValueError):
                print("that is not a valid answer")
                w= True
        if check == True:
            pass
            # can I call this function within this function
        return re

def confirm(m = "is this okay - y/n"):
    print (m)
    a = strcIn(allowed = ["n","y"], message = "y/n-->>")
    if a == "y":
        return True
    else:
        return False
        
        
        
def setupmatch(main):
        if main.state.currentMatch:
            match = main.state.currentMatch.number + 1
        elif main.state.lastMatch:
            match = main.state.lastMatch + 1
        else: 
            match = 0
        print("set-up next match: #", match, " ? ")
        i = strcIn(allowed = ["n","y"], message = "--y/n-->>")
        if i == "n":
            print ("what match to set-up: (number)", match)
            num = strcIn(typeInt = True, message = "match number>>")
            match = num
        
        def getRobots():# can this be done
            robots = []
            #enter red alliance
            robots.append(strcIn(typeInt = True, message ="Red alliance robot 1->>"))
            robots.append(strcIn(typeInt = True, message ="Red alliance robot 2->>"))
            robots.append(strcIn(typeInt = True, message ="Red alliance robot 3->>"))
            #enter blue alliance
            robots.append(strcIn(typeInt = True, message ="Blue alliance robot 4->>"))
            robots.append(strcIn(typeInt = True, message ="Blue alliance robot 5->>"))
            robots.append(strcIn(typeInt = True, message ="Blue alliance robot 6->>"))
            return robots
            
        c = False   
        while not c:
            robos=[]
            robos = getRobots()
            c = confirm()
            
        c = True
        while c:
            print("commit or escape")
            re = strcIn(message = ">>>>")
            if re == "commit":
                main.matchCreate(robos, match)
            if re == "escape" or re == "E":
                c = False#leave function
            
                