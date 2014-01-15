# user interface module


import cmd
import string, sys

#import main
import data
import joy


class com(cmd.Cmd): #global commands

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '

    def do_hello(self, arg):
        print("hello again", arg, "!")

    def help_hello(self):
        print("syntax: hello [message]")
        print("-- prints a hello message")

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
class ISP(com): #in setup commands
class RDC(com): #review data commands
class Test(com): #test commands
