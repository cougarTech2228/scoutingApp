# user interface module


import cmd
import string, sys

import main
import data
import joy

# just trying out cmd
class CLI(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '> '

    def do_hello(self, arg):
        print("hello again", arg, "!")

    def help_hello(self):
        print("syntax: hello [message]")
        print("-- prints a hello message")

    def do_quit(self, arg):
        sys.exit(1)

    def help_quit(self):
        print("syntax: quit")
        print("-- terminates the application")

    # shortcuts
    do_q = do_quit
