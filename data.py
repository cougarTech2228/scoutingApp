# Database module



class Competition(list):
    
    def __init__(self, numberOfMatches=0, name="Test"):
        # If numMatches = 0 then number of matches in competician is unknown
        # name is a name given for this competitian ex) 'FLR seeding', 'FLR
        # final', 'nationals Finals'
        self.name = name
        self.numMatches = numberOfMatches
        
    def newMatch(self, robots):
        # New Match takes a list of robot numbers as an argument
        self.inMatches=len(self)+1
        self.append(Match(self.inMatches, robots, self.name))
        
    def editMatch(self, matchNumber, teamNumbers):
        self[matchNumber-1] = Match(self.last_match, teamNumbers)




# an instance of a match with a number and six robot objects
class Match:
    
    def __init__(self, num, teamNumbers, compName):
        self.comp = compName
        self.number = num
        self.robots = [] # [0:2] red, [3:5] blue
        n = 0
        for teamNumber in teamNumbers:
            # This will create a new robot each time it is called,
            robots[n] = InMatchRobot(teamNumber,self, n, self.comp)
            n += 1  # [0:2] red, [3:5] blue
            pass
        
# An instance of a robot in one match in one competician, will be diffent for the same teams robot in diffent matches and competicians
class InMatchRobot:
    
    def __init__(self, teamNumber, myMatch, num, compName):
        self.comp = compName
        self.match = myMatch
        self.teamNumber = teamNumber
        self.num = num
        if allianceNumber < 3:
            self.alliance = 'RED'
        else:
            self.alliance = 'BLUE'

        records = InMatchRobotRecords(comp,self.match,self.teamNumber,self.alliance)

                        
class InMatchRobotRecords:
    def __init__(self, compName, myMatch, robot, ally):
        self.comp = compName
        self.match = myMatch
        self.roboNum = robot
        self.alliance = ally # string (RED or BLUE)
        
        
        pass
        # variables being recorded ex)shots missed, points scored, climberlevel reached
                
