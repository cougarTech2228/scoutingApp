#joystick interface module

import string, sys

import main

pause = False
end = False

_undoButton=10 # placeholder
inputs= []

class input:
 # a pointer to a joystick or other input device
 # will have bindings

    def __init__(self,N, myjoystick):
        myJoystick.init
        self.myJoystick = myJoystick
        self.bind = joyBindings()
        self.num = N
 
    def record(self,j, b):
        # will record event

        evt = self.bind.evtCheck(b)
        main.gameEvtInput(self.num, evt) 

    def getRobot(self):
        return self.robot

        
class joyBindings:
    def __init__(self):
        pass
        
    def evtCheck(button):
        if button == 0:
            evt = None#init a game event and return it
            return evt
        elif button == 1:
            evt = None#init a game event and return it
            return evt
        elif button == 2:
            evt = None#init a game event and return it
            return evt
        elif button == 3:
            evt = None#init a game event and return it
            return evt
        elif button == 4:
            evt = None#init a game event and return it
            return evt
        elif button == 5:
            evt = None#init a game event and return it
            return evt
        elif button == 6:
            evt = None#init a game event and return it
            return evt
        elif button == 7:
            evt = None#init a game event and return it
            return evt
        elif button == 8:
            evt = None#init a game event and return it
            return evt
        elif button == 9: 
            evt = None#init a game event and return it
            return evt       
        elif button == 10:
            evt = None#init a game event and return it
            return evt
        elif button == 11:
            evt = None#init a game event and return it
            return evt
        elif button == 12:
            evt = None#init a game event and return it
            return evt
        elif button == 13:
            evt = None#init a game event and return it
            return evt
        elif button == _undoButton:
                #undo some how
           return None#something
        else:

#       printf(mindblownyoloswaglol101chickenonaraft)
            sys.exit(1)#if this happens at least we will know the problem

        
def joystick_init(test = False):
    # get and check number of joysticks
    import pygame
    numJoy = pygame.joystick.get_count()

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
            inputs[i] = input(i, main.pygame.joystick.Joystick(i))
            
    return inputs

                        
 
     
def run():
    global pause, end ###is this needed (global)
    while not end:
         for evt in main.pygame.event.get():
             if not pause:
                 if evt.type == 10:
                    inputs[evt.joy].record(evt.button)
                    ##if echoOn and not command:
                    ##print("joystick: %s ---Button: %s  " % (evt.joy, evt.button))''' # possible later functionality echo
                     
             if evt.type == pygame.KEYDOWN:
                 if evt.key == K_SPACE:
                     main.toggle_pause()

    
