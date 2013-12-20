#database module

import main
import user
import joy

# an instance of a match with a number and six robot objects
class match:
	def __init__(num, robotNums):
		matchNum = num
		robots = []
		n = 0
		for r in robotNums:
			robots[n] = robot(r,n)
			n += 1
	
	
# an  instance of a robot with team number and alliance (will later have variables for collecting match data and possibly a variable for its joystick)
class robot:
	def __init__(team,roboNumber):
		if roboNumber <3:
			alliance = 0 
		else:
			alliance = 0
			
	