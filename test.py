# this is a testing class for testing code 

import sys

import pygame
from pygame.locals import *

import user
from sData import *
from data import *
import joy

RED = 1
BLUE = 2

# Main is the overarching program, which will be a portal to other branches
# like pit scouting, robot analysis, and match scouting
class Main():
    def __init__(self):
        self.matchList = Competition()
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
            #This whole section will be replaced by the command line module
            # what is used works as a temporary means of basic user input
            myAnswer = input(">>> ")

            if myAnswer == "start":
                self.start_match()
            elif myAnswer == "quit":
                break
            elif myAnswer == "robots":
                print(self.robotList)
            elif myAnswer == "matches":
                print(self.matchList)

                    

    # add_robots_from_file takes a file name as an argument and adds the entries,
    # each line is a team number, to the robotlist under main, as robot objects
    def add_robots_from_file(self, fileName="robots_test.txt"):
        file = open(fileName).readlines()
        for teamNumber in file:
            self.robotList.addRobot(Robot(teamNumber.strip()))


    # Initiates the match window
    def start_setup(self):
        self.gameEventList = GameEventList()
        
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption('CATS: CougarTech Scouting Application')
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 24)
        
    def start_match(self):
        self.start_setup()
        
        self.pause = True
        start = True

        self.points = 0

        #Main event loop for the match
        while True:

        # Looks through the event buffer for an input action
            for evt in pygame.event.get():

                #Quit out of window
                if evt.type == QUIT:
                    #The program should automatically save data before closing
                    pygame.quit()
                    break

                # Keyboard input to program (for those without a joystick)
                if evt.type == pygame.KEYDOWN:
                    if evt.key == K_SPACE:
                        self.toggle_pause()

                        
                    #Actions happen when the game isn't paused
                    if self.pause is False:
                        if evt.key == K_a:
                            self.add_auto_high()
                        elif evt.key == K_z:
                            self.add_auto_low()

                        elif evt.key == K_s:
                            self.add_tele_high()
                        elif evt.key == K_x:
                            self.add_tele_low()
                            
        # Redraw the screen
            self.screen.fill((0,0,0))

            # Pause message
            if self.pause is True:
                text = self.font.render("Press [space] to start", True, (255, 255, 255))
                self.screen.blit(text, (1, 1))

            else:
                pointsDisplay = self.font.render("Points: " + str(self.points), True, (255, 255, 255))
                self.screen.blit(pointsDisplay, (1, 1))

            # Update the display
            pygame.display.update()

            #prevents the session from running too fast
            self.clock.tick(40)

    def toggle_pause(self):
        self.pause = not self.pause

    #some dummy programs, do not actually represent point vaules, only for working with
    # key presses
    def add_auto_high(self):
        self.points += 15
    def add_auto_low(self):
        self.points += 15
    def add_tele_high(self):
        self.points += 5
    def add_tele_low(self):
        self.points += 1


# Start the Program
if __name__ == "__main__":
    myGame = Main()
    myGame.set_up()
    myGame.run()
    
    
