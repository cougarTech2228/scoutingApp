# user interface module


import cmd

import main



class Com(cmd.Cmd): #global commands

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '
        self.state = main.State() #This will create another instance of the main.State object.
                                  #I'm guessing that that isn't what you want
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
    def do_command(self, arg):
        if self.glob: # only want to do this once
            #command
    ''' 
    def do_setup(self):
        self.state.enterSetupMode()

    def do_matchMode(self):
        self.state.enterMatchMode()

    def do_quit(self, arg):
        
        if confirm(m = "quit (y/n)"):   
            main.quit()
        else:
                pass
        #sys.exit(1)

    def help_quit(self):
        print("syntax: quit")
        print("-- terminates the application")


    #match commands----------------------------------------------------------

    # shortcuts
    do_q = do_quit
     
    def do_p(self):
        self.state.togglePause()
            
    def do_pause(self):
        self.state.pauseSet(True)
        
    def do_start(self):
        self.state.startMatch()
        pass
        
    def do_end(self):
        self.state.endMatch()
        pass
        
    def do_restart(self):
        self.state.resetMatch(self)
        pass
    
    #setupcommands-----------------------------------------------------------
    
    def do_stm(self):
        self.state.inSetup =True
        setupmatch()
       
                
class Test(cmd.Cmd):
    
    def __init__(self):
        pass
        
            
    def do_testing(self, t):# stand for rendom thing i dont know what it is
        print("hello")



def init():
    
    Com().cmdloop()
 
    t = Test()
    t.cmdloop()
    
   
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
        
        
        
def setupmatch():
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
            r=[]
            r = getRobots()
            c = confirm()
        
        c = False
        while not c:
            c = True
            r = strcIn(message = ">>>>")
            if r == "commit":
                pass #do new match stuff
            if r == "escape" or r == "E":
                pass#leave function
            else:
                c = False
                