# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:23:38 2014

@author: team2228
"""
import readline
import data
import cmd
import os
import sys
import user

class Main():
    
    def __init__(self):
        self.getSaves()
        comp = input("which competition>>>")
        self.load(comp)
        self.data = Data(self.competition)
        cmdr(self)

        
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
            print("new competition:", fileName)
            print('--to save: type "save"')
            return False
            
    def getSaves(self):
        for file in os.listdir("resources/save_files/"):
            if file.endswith(".dat"):
                print ("    ",file)
                
class Data():
    def __init__(self, comp):
        self.competition = comp
        
    def printAll(self):
        for m in self.competition:
            print (m.number)
            for r in m.robots:
                print ("    ",r.teamNumber)
                
                try:
                    print(r.records.events.getMainList())
                    keys = r.records.records.keys()
                    print(keys)
                    print(list(keys))
                    for k in keys:
                        print("something")
                        f = r.records[k][0]
                        s = r.records[k][1]
                        a = f + s
                        print ("        ",k," attempted-",a," failures-",f," successes-",s)
                        
                except:
                    print("there is no records")                 
                   
    def printMD(self, level = 1, robots = None, matches = None):#scope is range of matches should be alist of numbers ex) [2,3,4,5,6,7]
        if not matches:
            matches = range(len(self.competition))
            
        for m in [self.competition[n-1] for n in matches]:
            print ("match",m.number)
            try:
                if m.notRun:
                    print("*")
            except:
                pass
            
            if level>=2:
                for r in m.robots:
                    print("    ",r.teamNumber)
                    if level==3:
                        keys = list(r.records.records.keys())
                        for k in keys:
                            f = r.records[k][0]
                            s = r.records[k][1]
                            a = f + s
                            print ("        ",k," attempted-",a," failures-",f," successes-",s)
                
                   
       
class cmdr():
    def __init__(self, main):
        cmd.Cmd.__init__(self)
        self.main = main
        self.data = main.data
        self.level = 1
        self.matches = []
        self.robots = []
        self.dats = []
        self.test()
        while True:
            c = input("# ")
            s = c.split()
            if len(s)==2:
                if s[0]== "+":
                    pass
                elif s[0]== "-":
                    pass
                elif s[0]== "m":
                    pass
                elif s[0]== "r":
                    pass
                elif s[0]== "d":
                    pass
                elif s[0]== "reset":
                    pass
                elif s[0]== "robot":
                    pass
                
    def robot(self):
        pass
    
    def test(self):
        self.data.printAll()
    '''
    def do_showMD(self,t):
        if "-l" in t:
            self.data.printMD(level = 3)
        elif "-s" in t:
            self.data.printMD(level = 1)
        else:
            self.data.printMD()
    
    def do_save(self,t):
        pass
    
    def do_search(self,t):
        try:
            n = t.split()[2]
            n = int(n)
        except:
            print("invalid")
            return
            
        if ("-m" in t) and ("-r" not in t):
            pass
       
        elif ("-m" not in t) and ("-r" in t):
            pass      
        
        else:
            print("invalid")
    
    def do_up(self, t):
        self.level[self.state] += 1
    
    def do_down(self, t):
        self.level[self.state] -= 1
    
    def do_scope(self, t):
        s = t.split()
        if "~" in t:
            self.scope[self.state] = None
            
        else:    
            try:
                self.scope[self.state]=[int(s[1]),int(s[2])]
                
            except TypeError:
                print("must be two INTEGERS")
                
            except IndexError:
                print("must be TWO")

    '''
    def do_quit(self, t):
        raise StopIteration
    '''  
    do_n = do_navigate
    do_u = do_up
    do_d = do_down
    '''
Main()