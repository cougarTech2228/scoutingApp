# main module
import pygame
from pygame.locals import *

import user
from data import *
import joy

RED = 1
BLUE = 2

class Main():
    def __init__(self):
        self.matchList = MatchList()
        self.robotList = RobotList()
        self.add_robots_from_file()
##        print(self.robotList)
        
        
        pygame.init()
        

    def set_up(self):
        pygame.init()
        pygame.event.set_allowed(10)
        terminalInterface = user.CLI()
        joy.joystick_init(True)

    def run(self):
        while 1:
            myAnswer = input(">>> ")

            if myAnswer == "start":
                self.start_match()
            elif myAnswer == "quit":
                break
            elif myAnswer == "robots":
                print(self.robotList)
            elif myAnswer == "matches":
                print(self.matchList)

                    


    def add_robots_from_file(self, fileName="robots_test.txt"):
        file = open(fileName).readlines()
        for teamNumber in file:
            self.robotList.addRobot(Robot(teamNumber.strip()))

    def start_match(self):
        pause = True
        start = True
        if start is True:
            for evt in pygame.event.get():
                #if evt.type == 10:
                #!!!if [(pygame.event.set_allowed(10)
                # (only allow button down events in the event list)]
                # works  then line unnecessary
                if evt.button == _undoButton:
                    undo(evt.joy)
                else:
                    record(evt.joy, evt.button)
                    '''if echoOn and not command: 
                    print("joystick: %s ---Button: %s  " % (evt.joy, evt.button))''' # possible later functionality echo

                if evt.type == pygame.KEYDOWN:
                    pass




if __name__ == "__main__":
    myGame = Main()
    myGame.set_up()
    myGame.run()
