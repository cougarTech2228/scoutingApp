# Database module

##import main
##import user
##import joy

class MatchList(list):
    
    def __init__(self, numMatches, name):
        # If numMatches = 0 then number of matches in competician is unknown
        # name is a name given for this competitian ex) 'FLR seeding', 'FLR
        # final', 'nationals Finals'
        self.current_match = 0
        self.last_match = 0
        ##self.append(0)
        
    def newMatch(self, robots):
        # New Match takes a list of robot numbers as an argument
        ##self[0] += 1
        self.append(Match(self.last_match, robotNums))

    def editMatch(self, matchNumber, robotNums):
        self[matchNumber-1] = Match(self.last_match, robotNums)




# an instance of a match with a number and six robot objects
class Match:
    
    def __init__(self, num, robotNums):
        self.number = num
        self.robots = [] # [0:2] red, [3:5] blue
        n = 0
        for teamNumber in robotNums:
            # This will create a new robot each time it is called,
            # We don't want that to happen for existing robots
            robots[n] = Robot(self, teamNumber, n)
            n += 1
	
	
# an  instance of a robot for a specific match in a specific competitian with team number and alliance (will later have variables for collecting match data and possibly a variable for its joystick)
class Robot:
    
    def __init__(self, myMatch, team, roboNumber):
        self.match = [myMatch]
        
        if roboNumber < 3:
            self.alliance = 'RED'
        else:
            self.alliance = 'BLUE'
        ##records = RobotRecords(Match.comp.name,myMatch.matchNum,alliance)

			
class RobotRecords:
    def __init__(self, comp, myMatch, robot, alliance):
        pass
        # variables being recorded ex)shots missed, points scored, climberlevel reached
                
