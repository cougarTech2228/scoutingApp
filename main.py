# Main module

# As of this build main.py is inoperational.
# To test the program, open test.py or run sData_test.py
import user

class Main():
    def __init__(self):
         pass
    def set_up(self):
        user.com()
         pass
     
class State():
    def __init__(self):
        self.inMatch = False
        self.inSetup = False
        self.inReview = False

        self.matchReadyStart = False
        self.matchReadyCommit = False
        self.matchPaused = False
        self.matchStopped = False
        self.matchRunning = False
        
    def getState(self):
        return self
        
    
