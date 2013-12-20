#This program might be getting a little to hot to handle
#I'm going to want to add some sort of logging feature soon, I'm going to want
#to find some way to export the list out, and import it again. [completed]
#Also find a way to display the robot list [completed]

from scoutingModule import *

class Core():
    def __init__(self):
        self.mainForm = Form()  #Form object is in scoutingModule, keeps code cleaner on this end
        self.roboRegister = RobotList() #The main object which will be manipulated

    def main(self):
        #Super simple main loop menu, if it doesn't see something it likes it complains
        #but doesn't crash
        quitApp = False
        while not quitApp:
            whatdo = self.mainForm.menu()
            if whatdo == "1": #add
                self.addNewBot()
            elif whatdo == "2": #remove
                self.removeBot()
            elif whatdo == "3": #display
                self.displayBots()
            elif whatdo == "4": #quit
                quitApp = True
            elif whatdo == "5": #save
                self.save()
            elif whatdo == "6": #load
                self.load()
            else:
                self.mainForm.typeError()
            
        
    def addNewBot(self):
        # adds a new entry into the list of robots
        robotData = self.mainForm.askNewBot()
        tmpRobot = Robot(robotData)
        self.roboRegister.addRobot(tmpRobot)
        if tmpRobot in self.roboRegister:
            self.mainForm.addBotConfirm()
        else:
            self.mainForm.generalError()

    def removeBot(self):
        # removes an entry from the list of robots
        robotNum = self.mainForm.deleteBot(self.roboRegister)
        self.roboRegister.removeRobotNum(robotNum)

    def displayBots(self):
        #lists all of the robots in the list on the screen, including stats
        self.mainForm.robotListHeader()
        for robot in self.roboRegister:
            self.mainForm.printRobot(robot)
        input()

    def save(self):
        #saves the robot list as a data file
        import pickle
        f = open(self.mainForm.saveFileName() + '.dat', "ab")
        pickle.dump(self.roboRegister, f)
        f.close()

    def load(self):
        #loads the robot list from a data  file
        import pickle
        f = open(self.mainForm.loadFileName() + '.dat', "rb")
        self.roboRegister = pickle.load(f)
        f.close()
        
    def test(self):
        #I don't think this needs to be in here anymore, but we'll see what may come of it.
        i = True
        while i:
            self.addNewBot()
            print(self.roboRegister)
            end = input("Do you want to add another robot?")
            if end.lower().strip() != "yes" and end.lower().strip() != "y":
                i = False

if __name__ == "__main__":
    newSession = Core()
    newSession.main()