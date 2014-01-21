# user interface module


import cmd
import string, sys

import main
import data
import joy


class com(cmd.Cmd): #global commands

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '
        self.state = main.State()
        triedCommand = ""
        
        updateState()
    
    def updateState(self):
        self.state = main.State.getState()

        
    def preCmd(self, line):
        self.updateState()
        return line
        
    #put global commands here
    def do_hello(self, arg):
        print("hello again", arg, "!")

    def failed_message(self):
	print("sorry, " triedCommand " is not a valid command")
	print("please refer to help for command information")


    #put global commands here

    def do_quit(self, arg):
        yn = input('are you sure y/n')
        main.quit()
        #sys.exit(1)

    def help_quit(self):
        print("syntax: quit")
        print("-- terminates the application")



    # shortcuts
    do_q = do_quit


class IMC(com): #in match commands
    def Cmd.precmd(self, line):
        updateState()
        if self.state.inMatch:
            return line
	else:
	    triedCommand = line
	    return "failed_message"

class ISC(com): #in setup commands
    def Cmd.precmd(self, line):
        updateState()
        if self.state.inSetup:
            return line
	else:
	    triedCommand = line
	    return "failed_message"

class RDC(com): #review data commands
    def Cmd.precmd(self, line):
        updateState()
        if self.state.inReview:
            return line
	else:
	    triedCommand = line
	    return "failed_message"

class Test(com): #test commands
    def Cmd.precmd(self, line):
        updateState()
        if self.state.inTest:
            return line
	else:
	    triedCommand = line
	    return "failed_message"

