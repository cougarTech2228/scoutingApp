#joystick interface module

import string, sys

#import main
import data
import user

pause = False
end = False
#joysticks = []
#eventHistory = []
#joyHistory = [[],[],[],[],[],[]]

_undoButton=10 # placeholder
inputs= []

class input:
 #this will have a pointer to a inMatchRobot and a pointer to a joystick(or other input device
 # will have bindings
    def __init__(self, myjoystick):
        myJoystick.init
        self.myJoystick = myJoystick
        
    def record(self, b):
        # will record event and increment data
        #global eventHistory, joyHistory
        #eventHistory.append([j,b])
        #joyHistory[j].append(b)
        main.gameEvtInput(self.robot,b) 
        pass

    def setRobot(self, records):
        
        self.robot = records

    def getRobot(self):
        return self.robot
		
def joystick_init(test = False):
    # get and check number of joysticks
    import pygame
    numJoy = pygame.joystick.get_count()

    #why is this here
    if test is True:
        numJoy = 6

    if numJoy == 6:
        print ("system detected 6 joysticks")
    elif numJoy < 6:
        print ("system detected %s joysticks \n this application needs at least 6 joysticks to work \n please plug in the required number of joysticks and try again" % (numJoy))
    elif numJoy > 6:
        print ("system detected %s joysticks \n this application needs only 6 joysticks to operate \n please note that one joystick will not be in use" % (numJoy))

	
    for i in range(numJoy):
        if test is not True:
            inputs[i] = input(main.pygame.joystick.Joystick(i))
            
                
    '''for i in range(numJoy): # append a array with number of buttons characters
        joystickrecords.append([])
        for b in range(self.joysticks[i].get_numbuttons()):
            joystickrecords[-1].append(0)'''
                        

	 
	 
def run(joyNum):
    global pause, end ###is this needed (global)
    while not end:
        if not pause:
            for evt in main.pygame.event.get():
                if evt.type == 10:#!!!if [(pygame.event.set_allowed(10)(only allow button down events in the event list)] works  then line unnecessary
                    inputs[evt.joy].record(evt.button)
                    ##if echoOn and not command:
                    ##print("joystick: %s ---Button: %s  " % (evt.joy, evt.button))''' # possible later functionality echo

                if evt.type == pygame.KEYDOWN:
                    if evt.key == K_SPACE:
                        main.toggle_pause()

	
