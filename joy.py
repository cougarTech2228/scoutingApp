#joystick interface module

import string, sys

import main
import data
import user

joysticks =[]


def joystick_init():
	
	# get and check number of joysticks
    numJoy = main.pygame.joystick.get_count()
    if numjoy = 6
		print ("system detected 6 joysticks")
	elif numjoy < 6
		print ("system detected %s joysticks /n this application needs at least 6 joysticks to work /n please plug in the required number of joysticks and try again" % (numJoy))
		break
	elif numjoy > 6
		print ("system detected %s joysticks /n this application needs only 6 joysticks to operate /n please note that one joystick will not be in use" % (numJoy))

	
    for i in range(numJoy):
        joysticks.append (main.pygame.joystick.Joystick(i))
        joysticks[i].init()
                
    '''for i in range(numJoy): # append a array with number of buttons characters
        joystickrecords.append([])
        for b in range(self.joysticks[i].get_numbuttons()):
            joystickrecords[-1].append(0)''' # data module will handle records
                        
	
def run():
	while !user.stop
		for evt in main.pygame.event.get():
			if evt.type == 10:#!!!if [(pygame.event.set_allowed(10)(only allow button down events in the event list)] works  then line unnecessary
				record(evt.joy, evt.button)
				'''if echoOn and not command: 
					print("joystick: %s ---Button: %s  " % (evt.joy, evt.button))''' # possible later functionality echo

def record(j,b):
     # this function is a shell 
	 # will record event and increment data