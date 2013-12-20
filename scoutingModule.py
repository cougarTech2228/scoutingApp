#This is the library of robot related objeccts
#to be used in the planned cougarTech scouting application


class RobotList(list):
    """This class inherits from the list class, it will handle all robot objects"""
##    def __init__(self):
##        self.robotList = []
##        self.robotKeys = []


    def __str__(self):
        return str([robot.robotNum for robot in self])

    def addRobot(self, robot):
        """
        if the list is empty it just adds the robot, like wise if it is
        the largest member of the list.  Otherwise it places the robot before
        the next greatest number through a binary search
        """
        #at this point if two different robots share the same number,
        #it will try to add the robot, but may end up freaking out.
        if robot in self:
            return False
        elif self == []:
            self.append(robot)
        elif robot.robotNum >= self[-1].robotNum:
            self.robotList.append(robot)
        else:
            index = self._binSearchIndex(robot.robotNum)
            self.insert(index, robot)
        self.robotKeys = [robot.robotNum for robot in self]
        #update the key List
        return True


    def getRobot(self, robotNum):
        #get a robot specified by it's id (number)
        pass

    def removeRobot(self, robot):
        #Try statement scheduled to be removed, will take care of error handly in Form
        try: self.remove(robot)

        except:
            "I need to look up what goes here"
            pass

    def removeRobotNum(self, robotNum):
        #removes a robot based on it's number
        robotVar = self.getRobot(robotNum)
        self.removeRobot(robotVar)

    def _binSearchIndex(self, robotNum):
        #after much consternation this works!, it returns the index of the lowest
        #roboNum above the given one
        import math
        tmpRoboList = self[:]
        while len(tmpRoboList) != 1:
            tmpIndex = math.ceil(len(tmpRoboList)/2) - 1 #Splits the list in half, bias towards lower number, just what I need!
            if robotNum < tmpRoboList[tmpIndex].robotNum:
                tmpRoboList = tmpRoboList[:(tmpIndex+1)]

            elif robotNum > tmpRoboList[tmpIndex].robotNum:
                tmpRoboList = tmpRoboList[(tmpIndex+1):]
                
        return self.index(tmpRoboList[0]) #returns the index of the robot just greater than the tested one, I hope


class Robot():
    #Really rudimentary robot object.  Don't need a complex one yet
    def __init__(self, robotData):
        self.robotNum = robotData["teamNumber"]
        self.weight   = robotData["Weight"]
        self.height   = robotData["Height"]
        self.length   = robotData["Length"]
        self.width    = robotData["Width"]
        
        self.R = 0 #number of rounds robot has been in

        self.data = {} #A dictionary of lists of length R (the number of Rounds robot has played in)
    def update(self, stats):
        #This function gets a list of new stats to add
        #maybe stats should be a dictionary, so we can iterate over the same keys as self.data
        self.R += 1
        pass

    def edit(self, stats, R):
        pass


class Form():
    #I/O class, This class receives data, then passes it to the core class as a tuple
    def __init__(self):
        pass

    def askNewBot(self):
        #asks the user what the Number for the robot is
        FIELDS = ("Weight", "Height", "Length", "Width")
        pitData = {}
        robotNum = int(input("What Number is the robot?: "))
        pitData["teamNumber"] = robotNum
        #Team number is a required field
        for field in FIELDS:
            entry = input(field + ": ")
            if entry:
                pitData[field] = entry
            else:
                pitData[field] = "None"
        return pitData

    def deleteBot(self, botList):
        robotNum = int(input("What Number is the robot?: "))
        if robotNum not in botList.robotKeys:
            print("Error: Robot not in list")
            return False
        #most of the stuff I'm putting in this function should go into core
        else:
            return robotNum
        
    def submit(self, robot):
        #gives the robot the stats tuple, I'll assemble it myself, It will be idiot proof. (with the exception of myself)
        #This needs to change, I'm going to let the core handle this one
        stats = ()
        robot.update(stats)

    def menu(self):
        print("--------------------------------------------------" + "\n" +
              "CATS: CougarTech Scouting Application" + "\n" +
              "--------------------------------------------------" + "\n" +
              "\n" +
              "Choose an option [1-3]:" + "\n" +
              "\t(1) Add a new robot to the register" + "\n" +
              "\t(2) Remove a robot from the register" + "\n" +
              "\t(3) View Robot List" + "\n" +
              "\t(4) Quit the application" + "\n" +
              "\n"*10)
        answer = input(": ")
        return answer

    def addBotConfirm(self):
        input("The robot was added successfully")

    def printRobot(self, robot):
        print(str(robot.robotNum) + "\t" +
              str(robot.weight) + "\t" +
              str(robot.height) + "\t" +
              str(robot.length) + "\t" +
              str(robot.width))

    def robotListHeader(self):
        print("Number\tWeight\tHeight\tLength\tWidth")
        print("-"*48)

    def saveFileName(self):
        fileName = input("What do you want to name your file?: ")
        return fileName

    def loadFileName(self):
        fileName = input("What is the name of your file?: ")
        return fileName
    
    def generalError(self):
        input("There was an error :(")
    
    def typeError(self):
        input("You're entry is invalid, please try again")
        
    def wipError(self):
        input("This part of the program is not functional, please try again")

if __name__ == "__main__":
    #This is just for developing purposes, I want a check to make sure the module is working as expected
##    newSession = Core()
##    newSession.test()
    pass