#database module

import main
import user
import joy

class competition:
    def __init__(numMatches, name):
        #if numMatches = 0 then number of matches in competician is unknown
        #name is a name given for this competitian ex) 'FLR seeding', 'FLR final', 'nationals Finals'
        matchList[]
        matchlist.append(0)
    def newMatch(robots):
        matchList[0] += 1
        matchlist.append(match(self, matchList[0], robots))
    
        
            
        

# an instance of a match with a number and six robot objects
class match:
	def __init__(comp, num, robotNums):
		matchNum = num
		robots = [] # 0-2 red, 3-5 blue
		n = 0
		for r in robotNums:
			robots[n] = robot(self, r,n)
			n += 1
	
	
# an  instance of a robot for a specific match in a specific competitian with team number and alliance (will later have variables for collecting match data and possibly a variable for its joystick)
class robot: 
	def __init__(myMatch, team,roboNumber):
		if roboNumber <3:
			alliance = RED
		else:
			alliance = BLUE
        records = roboRecords(match.comp.name,myMatch.matchNum,alliance)
			
class roboRecords:
    def __init__(comp, myMatch, robot, alliance)
        # variables being recorded ex)shots missed, points scored, climberlevel reached
                
