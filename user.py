# user interface module


import cmd
import string, sys
import time

import main
import data
import joy


class Com(cmd.Cmd): #global commands

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '
        self.state = main.State() #This will create another instance of the main.State object.
                                  #I'm guessing that that isn't what you want
        self.triedCommand = []
        self.glob = True #is this the top level command interpreter short for  global now unneeded
        self.allFailed = None
        
        self.updateState()
    
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
        yn = input('are you sure y/n')
        main.quit()
        #sys.exit(1)

    def help_quit(self):
        print("syntax: quit")
        print("-- terminates the application")

    def updateState(self):
        pass

    # shortcuts
    do_q = do_quit


class IMC(cmd.Cmd): #in match commands
    def __init__(self):
        pass
    def preCmd(self, line):
        if self.state.inMatch:
            return line
        else:
            return ""
            
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
        

class ISC(Com): #in setup commands
    def __init__(self):
        pass

    def precmd(self, line):
        if self.state.inSetup:
            return line
        else:
            return ""
    
    def do_stm():
        if self.state.currentMatch:
            match = self.state.currentMatch.number + 1
        elif self.state.lastMatch:
            match = self.state.lastMatch + 1
        else: 
            match = 0
        print("set-up next match: #", match, " ? ")
        i = strcIn(allowed = ["n","y"], message = "--y/n-->>")
        if i == "n"
            print ("what match to set-up: (number)", match)
            num = strcIn(typeInt = True, message = "match number>>")
            match = num
        
        
        
            
        
                
            
class RDC(Com): #review data commands
    def __init__(self):
        pass
        
    def precmd(self, line):
        if self.state.inReview:
            return line
        else:

            return ""

class Test(Com): #test commands
    def __init__(self):
        pass
        
    def precmd(self, line):
        if self.state.inTest:
            return line
        else:
            return ""

def do_init():
    Com()
    IMC()
    ISC()
    RDC()
    Test()
   
def strcIn(allowed = none, message = "", typeInt = False, check = False)
    w = True:
    while w:
        re = input(message):
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
                W = True
        if check = True
            pass
            # can I call this function within this function
        return re
    
            