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
        self.state = main.State()
        self.triedCommand = []
        self.glob = True #is this the top level command interpreter short for  global
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
    def do_matchMode(self):
        if self.glob: # only want to do this once
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


class IMC(Com): #in match commands
    def __init__(self):
        self.glob = False
        
    def preCmd(self, line):
        if self.state.inMatch:
            return line
        else:
            triedCommand.append(line)
            return "failed_message"
            
    def do_pause(self):
        self.state.togglePause()
            
    def do_start(self):
        self.state.startMatch()
        pass
        
    def do_end(self):
        self.state.endMatch()
        pass
        
    def do_restart(self):
        self.state.resetMatch(self)
        pass
        
    do_p = do_pause

class ISC(Com): #in setup commands
    def __init__(self):
        self.glob = False
        

    def precmd(self, line):
        if self.state.inSetup:
            return line
        else:
            triedCommand.append(line)
            return "failed_message"

class RDC(Com): #review data commands
    def __init__(self):
        self.glob = False
        
    def precmd(self, line):
        if self.state.inReview:
            return line
        else:
            triedCommand.append(line)
            return "failed_message"

class Test(Com): #test commands
    def __init__(self):
        self.glob = False
        
    def precmd(self, line):
        if self.state.inTest:
            return line
        else:
            triedCommand.append(line)
            return "failed_message"

def do_init():
    Com()
    IMC()
    ISC()
    RDC()
    Test()
    
