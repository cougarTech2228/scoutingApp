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
        self.bind = Bind(main)
        self.number = N
        self.type = "joystick" #FOR NOW
        self.main = main
        self.buttonBuffer = []
        
    def record(self, b,time):
        # will record event
        #possible laterfunctionality time to reconstruct matches in real time
        
        self.buttonBuffer.append([b,time])
        
        if b == self.bind.UNDO:
            if not self.bind.isAttribute(self.buttonBuffer[-2]):
                self.buttonBuffer.remove[-1]
                self.buttonBuffer.remove[-1]
            else:
                pass#complicated undo code
                
        elif self.bind.isAttribute(b) and self.bind.isEvt(self.buttonBuffer[-2]):
            evt = self.bind.makeEvent(self.buttonBuffer)
            self.main.connect.portEvt(self, evt) 
        
class Bind():
    def __init__(self, main):
        self.UNDO = 8
        self.SUCCESS = 11
        self.FAILURE = 10
        self.main = main
    
    def isAttribute(self, button):
        if button == self.SUCCESS:
            return True
        elif button == self.FAILURE:
            return True
        else:
            return False
            
    def isEvent(self, button):
        if button in [1,2,3,4,5,9,6,7]:
            return True
        else:
            return False
        
    def makeEvent(self, buttonBuffer):
        attribute = buttonBuffer[-1][0]
        event = buttonBuffer[-2][0]
        timespan = [buttonBuffer[-2][1],buttonBuffer[-1][1]]
        #at this time timespan is not used- possible later functionality
        
        
        
class Joy():
    def __init__(self, main, test = False):
        # get and check number of joysticks
        pygame.init()
        pygame.joystick.init()
        pygame.event.set_blocked(7)
        pygame.event.set_blocked(11)
        self.inputObs= []
        self.stopRun =False
        self.main = main
        self.test = test
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
                
    
    def reset(self):
        self.stopRun = True                        
        self.__init__(self.main, self.test)
        self.stopRun = False
         
    def getInputs(self):
        return self.inputObs
         
    def run(self, state, main):
        print("record on")
        while not state.exit:
            first = True
            while state.matchRunning and not state.exit and not self.stopRun:
                 if first:
                     pygame.event.get()
                     first = False
                     
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
            if first == False:
                pass #get third axis for rating of robot preformance
                     
    def check(self, state, main): #check once then return this does not work
        import pygame
        if state.matchRunning:
            for evt in pygame.event.get():
                 if not state.matchPaused:
                     if evt.type == 10:
                        self.inputObs[evt.joy].record(evt.button, )
                        if state.echoOn:
                            print("joystick: %s ---Button: %s  " % (evt.joy, evt.button))
                        
                        
                 if evt.type == pygame.KEYDOWN:
                     if evt.key == pygame.K_SPACE:
                         state.toggle_pause()
                        
    def getJoy(self):
        while True:
            evt = pygame.event.wait()
            if evt.type == 10:
                return(self.inputObs[evt.joy])