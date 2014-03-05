#joystick interface module
import datetime
import pygame
import data
_undoButton=10 # placeholder

class inputOb:
 # a pointer to a joystick or other input device
 # will have bindings

    def __init__(self,N, myJoystick, main):
        self.myJoystick = myJoystick
        self.myJoystick.init()
        if N > 2:
            self.type = "Controller"
            print("controller ", N, " initialised")
        else:
            self.type = "joystick" 
            print("joystick ", N, " initialised")

        self.bind = Bind(main, self.type)
        self.number = N
        self.main = main
        self.buttonBuffer = []
        
    def record(self, b,time):
        # will record event
        #possible laterfunctionality time to reconstruct matches in real time
        self.buttonBuffer.append([b,time])
        if self.main.state.echo: print("button press recieved")

        try:
            if b == self.bind.UNDO:
                if self.bind.isEvent(self.buttonBuffer[-2]):
                    self.buttonBuffer.pop(-1)
                    self.buttonBuffer.pop(-1)
                else:
                    pass#complicated undo code
                 
             
            
            elif self.bind.isAttribute(b) and self.bind.isEvent(self.buttonBuffer[-2][0]):
                if self.main.state.echo: print("is attribute")
                evt = self.bind.makeEvent(self.buttonBuffer)
                if self.main.state.echo: print("recieved event and sending to connector")
                if evt:
                    self.main.connect.portEvt(self, evt)
                    
        except IndexError:
            pass
            
            
class Bind():
    def __init__(self, main, mode = "Joystick"):
        if mode == "Controller":
            self.UNDO = 3
            self.SUCCESS = 1
            self.FAILURE = 2
            
            self.LowGoal = 4
            self.HighGoal = 5
            self.Pass = 6
            self.Receive = 7
            self.TrussThrow = 10
            self.TrussCatch = 11
            self.Penalty = None#set to hat button
            self.BlockGoal = 0
            self.MoveForward = 0
            
        else:#joysticks
            self.UNDO = 8
            self.SUCCESS = 10
            self.FAILURE = 9
            
            self.LowGoal = 1
            self.HighGoal = 2
            self.Pass = 3
            self.Receive = 4
            self.TrussThrow = 0
            self.TrussCatch = 7
            self.BlockGoal = 5
            self.Penalty = None  #set to hat button
            self.MoveForward = 0 
                                 
        self.main = main
        self.mode = mode
    
    def isAttribute(self, button):
        if button == self.SUCCESS:
            return True
        elif button == self.FAILURE:
            return True
        else:
            return False
            
    def isEvent(self, button):
        if button not in [self.SUCCESS, self.FAILURE,self.UNDO]:
            return True
        else:
            return False
            
    def makeEvent(self, buttonBuffer):
        if self.main.state.echo: print("making event")
        timespan = [buttonBuffer[-2][1],buttonBuffer[-1][1]]
        
        if buttonBuffer[-1][0] == self.SUCCESS:
            success = True
            if self.main.state.echo: print("success")
        elif buttonBuffer[-1][0] == self.FAILURE:
            success = False
            if self.main.state.echo: print("failure")
        else:
            print("lacking attribute error")
            raise
            
        button = buttonBuffer[-2][0]
        
        if self.main.state.autonomous:
            if self.main.state.echo: print("auto")
            if button == self.MoveForward:
                return data.Auto_MoveForwandEvent(success)
                     
            elif button == self.LowGoal:
                return data.Auto_LowGoalEvent(success)
            
            elif button == self.HighGoal:
                return data.Auto_HighGoalEvent(success)
                
            elif button == self.BlockGoal:
                return None#temporary 
                
            else:
                return None
            
        else:
            if self.main.state.echo: print("tele-op")
            if button == self.LowGoal:
                return data.LowGoalEvent(success)
                
            elif button == self.HighGoal:
                return data.HighGoalEvent(success)
                
            elif button == self.TrussThrow:
                return data.TrussThrowEvent(success)
            
            elif button == self.TrussCatch:
                return data.TrussCatchEvent(success)
                
            elif button == self.Pass:
                return data.AssistPassEvent(success)
                
            elif button == self.Receive:
                return data.AssistRecieveEvent(success)
                
            elif button == self.BlockGoal:
                return None#temporary
            
            else:
                return None
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
                 if not state.matchPaused:
                     if evt.type == 10:
                        if state.echo: print("button pressed")
                        self.inputObs[evt.joy].record(evt.button, datetime.datetime.now())
                        
                        '''
                     if evt.type == 9:
                        self.inputObs[evt.joy].recordHat(evt.value)
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