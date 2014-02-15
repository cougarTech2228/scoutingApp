#joystick interface module
import datetime
import pygame
_undoButton=10 # placeholder

class inputOb:
 # a pointer to a joystick or other input device
 # will have bindings

    def __init__(self,N, myJoystick, main):
        print("joystick ", N, " initialised")
        self.myJoystick = myJoystick
        self.myJoystick.init()
        self.bind = joyBindings()
        self.number = N
        self.type = "joystick" #FOR NOW
        self.main = main
    def record(self, b,time):
        # will record event
        #possible laterfunctionality time to reconstruct matches in real time
        evt = self.bind.evtCheck(b)
        self.main.data.gameEvtRecord(self.number, evt) 

    def getRobot(self):
        return self.robot

#This should be done with pygame, they have an elegent method of handling it.        
class joyBindings:
    def __init__(self):
        pass
        
    def evtCheck(self, button):
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
           pass
class Joy():
    def __init__(self, main, test = False):
        # get and check number of joysticks
        pygame.init()
        pygame.joystick.init()
        pygame.event.set_blocked(7)
        pygame.event.set_blocked(11)
        self.inputObs= []
        numJoy = pygame.joystick.get_count()
        
        if test:
            print ("system detected %s joysticks -- test is true" % (numJoy))
            for i in range(numJoy):
                pygame.joystick.Joystick(i).init()
                self.inputObs.append(inputOb(i, pygame.joystick.Joystick(i), main))
        else:
                
            if numJoy == 6:
                print ("system detected 6 joysticks")
                
            elif numJoy < 6:
                print ("system detected %s joysticks \n this application needs at least 6 joysticks to work \n please plug in the required number of joysticks and try again" % (numJoy))
                main.state.exit = True    
                return
                
            elif numJoy > 6:
                print ("system detected %s joysticks \n this application needs only 6 joysticks to operate \n please note that one joystick will not be in use" % (numJoy))    
            
            for i in range(numJoy):
                self.inputObs[i] = input(i, pygame.joystick.Joystick(i), main)
                
    
                            
     
         
    def run(self, state, main):
        print("record on")
        while not state.exit:
            while state.matchRunning and not state.exit:
                 evt = pygame.event.poll()
                 if evt.type is not 0:
                     print(evt)
                 if not state.matchPaused:
                     if evt.type == 10:
                        self.inputObs[evt.joy].record(evt.button, datetime.datetime.now())
                        ##if echoOn and not command:
                        ##print("joystick: %s ---Button: %s  " % (evt.joy, evt.button))''' 
                        # ^possible later functionality echo^
                 '''     
                 if evt.type == pygame.KEYDOWN:
                     if evt.key == pygame.K_SPACE:
                         state.toggle_pause()
                 '''
                     
    def check(self, state, main): #check once then return this does not work
        import pygame
        if state.matchRunning:
            for evt in pygame.event.get():
                 if not state.matchPaused:
                     if evt.type == 10:
                        self.inputObs[evt.joy].record(evt.button, )
                        ##if echoOn and not command:
                        ##print("joystick: %s ---Button: %s  " % (evt.joy, evt.button))''' 
                        # ^possible later functionality echo^
                        
                 if evt.type == pygame.KEYDOWN:
                     if evt.key == pygame.K_SPACE:
                         state.toggle_pause()
                        
                
