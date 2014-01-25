import data

class Main():

    def __init__(self):
        self.competition = data.Competition("Test")
        
    
    def add_matches_from_file(self, fileName="matches.txt"):
        file = open(fileName, "r")
        for line in file:

            eol = False #end of line
            firstWord = True
            matchNum = 0
            robotNums = []
            
            if line[0] == "#":
                print("pass")
                eol = True    
            
            while not eol:
                word = ""
                for letter in line:
                    
                    if letter == " " or letter == "\t": #a space or tab
                        if firstWord is True:
                            matchNum = int(word)
                            print("Match Number: " + word)
                            firstWord = False
                            word = ""
                        else:
                            robotNums.append(int(word))
                            print("Robot Number: " + word)
                            word = ""
                            
                    elif letter == "\n" or letter == "\r":
                        eol = True
                        
                    else:
                        word += letter
                        
            if matchNum != 0:
                self.competition.newMatch(robotNums, matchNum)

if __name__ == "__main__":
    myTest = Main()
    myTest.add_matches_from_file()
