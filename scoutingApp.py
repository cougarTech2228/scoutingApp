import pygame, sys
import threading
import time
from pygame.locals import *

# start pygame	
pygame.init()

class ScoutingApp:

    def __init__(self):
        #list of joystick objects and total presses of each button
        self.joystickRecords = [] 
        self.joysticks =[]
        self.robots = []

        #command constants
        self.comPause = ['stop','Stop','STOP','!p','pause']
        self.comEnd = ['!term','!eom','!end']
        self.comSetup = ['!su','setup']
        self.comStart = ['!run']
        self.comEcho = ['!echo','echo']
        self.comHelp = ['!h','help','Help','HELP']
        self.comCom = ['','\r']
                
        #command variables
        self.echoOn = False
        self.command = True
        self.end = False
        self.pause = False

    
    #set-up the joystick data array
    def prepare(self):
        numJoy = pygame.joystick.get_count()
        #print (numJoy)


        for i in range(numJoy):
            self.joysticks.append (pygame.joystick.Joystick(i))
            self.joysticks[i].init()
                    
        for i in range(numJoy): # append a array with number of buttons characters
            self.joystickRecords.append([])
            for b in range(self.joysticks[i].get_numbuttons()):
                self.joystickRecords[-1].append(0)
                            
        pygame.event.set_allowed(10) #only allow button down events in the event list
            
    #run the button press grab event loop
    def run(self):
        while not self.end:
            if not self.pause:	
                if pygame.event.peek(10):
                    for evt in pygame.event.get():
                        if evt.type == 10:#!!!if (pygame.event.set_allowed(10) #only allow button down events in the event list) works  then line unnecessary
                            self.record(evt.joy, evt.button)
                            if echoOn and not command: 
                                print("joystick: %s ---Button: %s  " % (evt.joy, evt.button))
                else:
                    time.sleep(.05)

    def setup(self):
        # enter robots in match
        e = False
        while not e:
            for i in range(6):
                self.robots.append([0,'',0])#(number,team(red, blue), joystick)
                if i<3:    
                    self.robots[-1][0] = input('Input Red Allience Bot # %s: ' % (i+1));
                    self.robots[-1][1] = 'red'
                if i>=3:    
                    self.robots[-1][0] = input('Input Blue Allience Bot # %s: ' % (i-2));
                    self.robots[-1][1] = 'blue'
            
            for i in range(6):
                print ('\n' + self.robots[i][0] + ' ' + self.robots[i][1])

            yn = '' #yes/no answer

            #Comfirm entries
            while yn != 'y' and yn != 'n':
                yn = input('are these names and teams correct - y/n: ').lower()
                if yn != 'y' and yn != 'n':
                    print ('That is not A valid answer')

                    
            if yn == 'n':
                del self.robots[-1] #removes the last (incorrect) entry
                yn = ''
                continue
            else:
                e = True #this ends the loop

            for i in range(6):
                pass
                # this is where i felt like stopping next step is to grab which joysticks map to which robots


    #record a button press
    def record(self,j,b):
            self.joystickRecords[j][b] += 1
    
    #process the command
    def commandCheck(self, com):
        if com in self.comEnd:
            pass

        elif com in self.comStart:
            pass

        elif com in self.comSetup:
            self.setup()

        elif com in self.comHelp:
            f = open('help.txt', 'r')
            print (df.read())
            f.close()

        elif com in self.comPause:
            self.pause = not self.pause
            
        elif com in self.comCom:
            self.command = not self.command
                            
        elif com in self.comEcho:
            self.echoOn = not self.echoOn
		

if __name__ == "__main__":
    scoutingApp = ScoutingApp()
##    scoutingApp.setup()
    scoutingApp.prepare()
    scoutingApp.run()

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
