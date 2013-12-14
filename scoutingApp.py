import pygame, sys
import threading
import time
from pygame.locals import *

#variable creation------------------------------------------------------------

	#list of joystick objects and total presses of each button
	joystickrecords = [] 
	joysticks =[]
    robots = []
	#command constants
		comPause = ['stop','Stop','STOP','!p','pause']
        comEnd = ['!term','!eom','!end']
		comSetup = ['!su','setup']
		comStart = ['!run']
		comEcho = ['!echo','echo']
		comHelp = ['!h','help','Help','HELP']
		comCom = ['','/r']
		
	#command variables
		echoOn == False
		command == True
		end == False
		pause == False

	
		
		
	
#functions and app setup-------------------------------------------------------

	# start pygame	
	pygame.init()


	#set-up the joystick data array
	def prepare():
		numJoy = pygame.joystick.get_count()
			#print (numJoy)


		for i in range(numJoy):
			joysticks.append (pygame.joystick.Joystick(i))
			joysticks[i].init()
			
		for i in range(numJoy): # append a array with number of buttons characters
			joystickrecords.append([])
			for b in range(self.joysticks[i].get_numbuttons()):
				joystickrecords[-1].append(0)
				
		pygame.event.set_allowed(10) #only allow button down events in the event list
		
		
	#record a button press
	def record(self,j,b):
		joystickrecords[j][b] += 1 
		
	#run the button press grab event loop
	def run():
		while True:
			if !pause:	
				if pygame.event.peek(10):
					for evt in pygame.event.get():
						if evt.type == 10:#!!!if (pygame.event.set_allowed(10) #only allow button down events in the event list) works  then line unnecessary
							record (evt.joy, evt.button)
							if echoOn & !command 
								print("joystick: %s ---Button: %s  " % (evt.joy, evt.button))
				else:
					sleep(.05)
			if end:
				break
    def setup
        # enter robots in match
        while True:
            for i in range(6):
                robots.append([0,'',0])#(number,team(red is one, blue is two), joystick)
                if i<3    
        		    robots[-1][1] = input('Input Red Allience Bot # %s' % (i+1));
                    robots[-1][2] = 'red
	            if i<3    
        		    robots[-1][1] = input('Input Blue Allience Bot # %s' % (i-2));
                    robots[-1][2] = 'blue'
            while True:
                for i in range(6):
                    print ('/n' + robots[i][1] + robots[i][1])
                yn = input('are these names and teams correct - y/n')
                if yn == 'y':
                    break
                elif yn == 'n':
                    break
                else: 
                    print ('That is not A valid answer') 
            if yn == 'n':
                yn = ''
                continue

            for i in range(6):
                # this is where i felt like stopping next step is to grab which joysticks map to which robots
            
	#process the command
	def commandCheck(com):
		if com in comEnd:
		elif com in comStart:
		elif com in comSetup:
            setup()
		elif com in comHelp:
            f = open('help.txt', 'r')
            print f.read()
            f.close()


        elif com in comPause:
            if pause
				pause=False
			if !pause 
				pause=True
		
		elif com in comCom:
			if command
				command=False
			if !command 
				command=True
				
		elif com in comEcho:
			if 	echoOn
				echoOn=False
			if !echoOn 
				echoOn=True
		





'''for joy in joysticks:
for button in range(joy.get_numbuttons()):
if joy.get_button(button)== 1:
record (button, joy.get_id())
if evt.type == QUIT:
pygame.quit()
sys.exit()
if evt.type == !end:'''
''''__package__']
>>> from pygame.constants import *
>>> JOYBUTTONDOWN
10
>>> import threading
>>> def foo() :
...     for i in range(10) :
...           print(i)
...           time.sleep(10)
...
>>> import time
>>> t = threading.thread(target=foo)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'thread'
>>> t = threading.Thread(target=foo)
>>> t.start()
>>> 0

>>>
>>>
>>>
>>> foo
<function foo at 0x012C54F8>
>>> 1

>>>
>>> 2

>>>
>>>
>>>
>>> 3

>>>
>>> 4

>>> t.5
kill
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Thread' object has no attribute 'kill'
>>> dir6
(t)
['_Thread__exc_info', '_Thread__initialized', '__class__', '__delattr__', '__dic
t__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
 '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__
', '__subclasshook__', '__weakref__', '_args', '_block', '_bootstrap', '_bootstr
ap_inner', '_daemonic', '_delete', '_ident', '_initialized', '_kwargs', '_name',
 '_note', '_reset_internal_locks', '_set_daemon', '_set_ident', '_started', '_st
derr', '_stop', '_stopped', '_target', '_verbose', 'daemon', 'getName', 'ident',
 'isAlive', 'isDaemon', 'is_alive', 'join', 'name', 'run', 'setDaemon', 'setName
', 'start']
>>> 7
8
9

>>>'''
