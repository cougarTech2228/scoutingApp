# Main module

# As of this build main.py is inoperational.
# To test the program, open test.py or run main_test.py
import threading
import time, sys, os


import datetime
import user
import data

class Main():
    def __init__(self):
        pass
    def start(self):
        self.data = Data(self)
        x = user.Com(self)
        x.cmdloop()
        
class Data(): 
    def __init__(self, main): #reminder -this must be fixed
        #if not self.load:
        print("\n competition save files...")
        self.getSaves()
        print("\n open or create a save file... \n")
        cstr = input("competition name? >>>")
        print ("\n \n")
        self.load(cstr)            
        self.main = main
            
    def getUndefinedMatch(self):
        for m in range(len(self.competition)):
            if self.competition[m] == None:
                return m+1 #returns match number
        return len(self.competition)+1
        
    def add_matches_from_file(self, fileName="matches.txt"):
        file = open(fileName, "r")
        for line in file:

            eol = False #end of line
            firstWord = True
            matchNum = 0
            robotNums = []
            
            if line[0] == "#":
                ##print("pass")
                eol = True    
            
            while not eol:
                word = ""
                for letter in line:
                    
                    if letter == " " or letter == "\t": #a space or tab
                        if firstWord is True:
                            matchNum = int(word)
                            ##print("Match Number: " + word)
                            firstWord = False
                            word = ""
                        else:
                            robotNums.append(int(word))
                            ##print("Robot Number: " + word)
                            word = ""
                            
                    elif letter == "\n" or letter == "\r":
                        eol = True
                        
                    else:
                        word += letter
                        
            if matchNum != 0:
                self.competition.newMatch(robotNums, matchNum)
                
    
    def add_robots_from_file(self, fileName="robots.txt"):
        file = open("./resources/"+fileName).readlines()
        for teamNumber in file:
            self.robots.addRobot(data.Robot(teamNumber.strip()))
        
    def save(self):
        import pickle
        save_file = open("resources/save_files/" + self.competition.name + ".dat", "wb")
        save_data = [self.competition,self.robots ]
        
        pickle.dump( save_data, save_file )
        save_file.close()
        print(self.competition.name,"competition saved")

    def load(self, fileName):
        import pickle
        try:
            load_data = pickle.load( open("resources/save_files/" + fileName + ".dat", "rb") )
            self.competition = load_data[0]
            self.robots = load_data[1]
            print("loaded save: ",fileName)
            return True
            
        except:
            self.competition = data.Competition(name = fileName)
            self.robots = data.RobotList()
            print("new competition:", fileName)
            print('--to save: type "save"')
            return False
            
    def getSaves(self):
        for file in os.listdir("resources/save_files/"):
            if file.endswith(".dat"):
                print ("    ",file)
                
                

    def destroySaves(self):
        files = [f for f in os.listdir(".\\")]
        print("this function is a bad idea- are you absolutely sure you want to delete ALL save files")
        if user.confirm():
            for file in files:
                if file[-3:] == "dat":
                    os.remove(file)
                    print()

        
if __name__ == "__main__": #This part is so that when it is imported, the following code doesn't run   
    if '-test' in sys.argv:
        tester =  True
    else:
        tester = False
    main = Main()
    main.start()




