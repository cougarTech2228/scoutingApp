# user interface module


import cmd
import sys
import os
import data

autosave = True

class Com(cmd.Cmd): #global commands

    def __init__(self, main):
        cmd.Cmd.__init__(self)
        self.main = main
        self.prompt = '>>>>>'   
    #setupcommands-----------------------------------------------------------    
    
    def do_inputMatch(self, t):
        try:
            inputMatch(self.main)
        except:
            pass
    def do_quit(self, t):
        if confirm(m = "quit (y/n)"):   
            self.main.data.save()
            sys.exit(1)
        else:
            pass
        
    def do_addRobots(self, t):
        ans = confirm(m="Do you want to read from robots.txt?", quit_=True)
        if ans == 0:
            return 0
            
        elif ans is True:
            self.main.data.add_robots_from_file()
            
        else:
            fileName = input("What file")
            self.main.data.add_robots_from_file(fileName)
        
    def do_review(self, t):
        if "-i" in t:
            try:
                import review

            except StopIteration:
                pass
        else:    
            os.system('./REVIEW.sh')
    
    def do_show(self, t):
        if "ds" in t:
            for m in self.main.data.competition:
                if m:
                    print("match ",m.number)
                    for r in m.robots:
                        print("    team ", r)
                        
        else:
            print("show needs a parameter")
                        
    def do_save(self, t):
        self.main.data.save()
        
    def do_debug(self, t):
        import pdb; pdb.set_trace()

    def help_save(self):
        print("syntax: save")
        print("shortcut: s")
        print("saves the game data to  <competition_name>.dat in ./resources/save_files")
                
                
    do_stm = do_inputMatch
    do_s = do_save
    help_s = help_save

def strcIn(allowed = None, message = "", typeInt = False, check = False, quit_ = True):
    while True:
        re = input(message)
        if re == "!E" and quit_:
            raise
        if allowed:
                if re not in allowed:
                    print("that is not a valid answer")
                    continue
        if typeInt:
            try:
                if re == "":
                    return 0
                v = int(re)
                re = v
            except (ValueError):
                print("that is not a valid answer")
                continue
                
        if check == True:
            if not confirm(re, safe = False):
                continue
            
        return re
    

def confirm(m = "is this okay", safe = True, quit_=False, weird=False):
    print (m)
    if safe and not weird:
        a = strcIn(allowed = ["n","y","Y","N","yes","no","Yes","No"], message = "y/n ->>")
        if a in ["y","Y","yes","Yes"]:
            return True
        elif a in ["n", "N", "no", "No"]:
            return False
            
    if weird:
        a = strcIn(allowed = ["n","y","Y","N","yes","no","Yes","No", "","!E"], message = "y/n-->>")
        if a in ["y","Y","yes","Yes"]:
            return True
        elif a == "!E":
            raise
        elif a in ["n", "N", "no", "No", ""]:
            return False
        else:
            return 0
            
    else:
        a = strcIn(allowed = ["n","y","Y","N","yes","no","Yes","No", "", "!E"], message = "y/n-->>")
        if a in ["y","Y","yes","Yes"]:
            return True
        elif a == "":
            return True
        elif a == "!E":
            raise
        else: 
            return False
        
        
def inputMatch(main, match=None): #nor  = number of robots per alliance
    if not match:
        match = get_matchNum(main)
    main.data.competition.newMatch(matchNum = match)
    for x in range(6):
        rn, ally = get_robot(main, x+1)
        print("robot ",rn)
        rrr = data.InMatchRobotRecords(match, rn, ally)      
        records = rrr.records

        records["move_forward_auto"] =confirm(m="moved forward in auto?", weird = True) 
        records["start_goalie_zone"] =confirm(m="started in goalie zone?", weird = True)         
        
         
        records["pass_success"] =strcIn(message = "Pass Success>>>",typeInt =True, check = True)
        records["pass_failure"] =strcIn(message = "Pass Failure>>>",typeInt =True,check = True)
        records["receive_success"] =strcIn(message = "Receive Success>>>",typeInt =True,check = True)
        records["receive_fail"] =strcIn(message = "Receive Failure>>>",typeInt =True,check = True)
        
        records["truss_throw_success"] =strcIn(message = "Truss Throw Success>>>",typeInt =True,check = True)
        records["truss_throw_success"] =strcIn(message = "Truss Throw Failures>>>",typeInt =True,check = True)   
        
        records["truss_catch_success"] =strcIn(message = "Truss Catch Success>>>",typeInt =True,check = True)
        records["truss_catch_success"] =strcIn(message = "Truss Catch Failures>>>",typeInt =True,check = True)   
        
        records["auto_high_goal_success"] =strcIn(message = "Autonomous High Goal Success>>>",typeInt =True,check = True)
        records["high_goal_success"] =strcIn(message = "High Goal Success>>>",typeInt =True,check = True)
        records["auto_high_goal_failure"] =strcIn(message = "Autonomous High Goal Failure>>>",typeInt =True,check = True)
        records["high_goal_failure"] =strcIn(message = "High Goal Failure>>>",typeInt =True,check = True)
        records["auto_low_goal_success"] =strcIn(message = "Autonomous Low Goal Success>>>",typeInt =True,check = True)
        records["low_goal_success"] = strcIn(message = "Low Goal Success>>>",typeInt =True,check = True)
        records["auto_low_goal_failure"] =strcIn(message = "Autonomous Low Goal Failure>>>",typeInt =True,check = True)
        records["low_goal_failure"] =strcIn(message = "Low Goal Failure>>>",typeInt =True,check = True)
        
        records["auto_blocking_success"] =strcIn(message = "Auto Goal Blocking Success>>>",typeInt =True,check = True)
        records["goal_blocking_success"] =strcIn(message = "Auto Blocking Success>>>",typeInt =True,check = True)
        records["auto_blocking_failure"] =strcIn(message = "Auto Goal Blocking Failure>>>",typeInt =True,check = True)          
        records["goal_blocking_failure"] =strcIn(message = "Goal Blocking Failure>>>",typeInt =True,check = True)
        records["pushing_def_success"] =strcIn(message = "Pushing/Defensive Success>>>",typeInt =True,check = True)
        records["pushing_def_failure"] =strcIn(message = "Pushing/Defensive Failure>>>",typeInt =True,check = True)
                
        rrr.penalties=strcIn(message = "Penalties? ")
        rrr.stagety=strcIn(message = "Stategy? ")
        rrr.comments.append(strcIn(message = "Comment? "))
        
        main.data.robots[rn].addMatch(rrr)
        main.data.competition[match-1].robots[rn]=rrr
        if autosave:
            main.data.save()            


        
        
def get_robot(main, num):# can this be done
    if num>3:
        alliance  = "BLUE"
    else:
        alliance = "RED"
    s = "enter " + alliance + " alliance robot number>>>" 
    while True:
        robotNumber = strcIn(message = s, typeInt = True)
        if robotNumber not in main.data.robots.keys():
            print("That robot isn't created yet")
            if confirm("Do you want to create that robot?"):
                from data import Robot
                main.data.robots.addRobot(Robot(robotNumber))
            else:
                continue
        return robotNumber, alliance
        
            
def get_matchNum(main):
    match = main.data.getUndefinedMatch()
    print("input next undefined match: #",match,"?" )
    if not confirm():
        
        if main.state.currentMatch:
            match = main.state.currentMatch.number + 1
        elif main.state.lastMatch:
            match = main.state.lastMatch.number + 1
        else:
            match = 1
            
        print("set-up next match: #", match, "? ")
        if not confirm():
            print ("what match to set-up: (number)")
            num = strcIn(typeInt=True, message="match number>>")
            match = num
            try:
                if main.state.currentMatch.number == match:
                    print("you cant setup that match, you are already in it")
                    return False
            except:
                pass
                
    try:
       if main.data.competition[match-1]:
            print("match already exists, would you like to override it.\n (this could be a destructive process)")
            if not confirm():
                return False
                
    except:
        pass
    
    return match
    
    

