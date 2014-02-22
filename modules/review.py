# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:23:38 2014

@author: team2228
"""

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
    def __init__(self,comp):
        self.competition = comp
    
    def printMD(level = 1, scope = None):#scope is range of matches should be alist of numbers ex) [2,3,4,5,6,7]
        for m in [competition[n-1] for n in scope]:
            print m.number
            if level>=2:
                for r in m.robots:
                    print(r.teamnumber)
                    if level>=3
                        for key in r.record.records:#must get keys
                            pass
        
                   
       
class cmdr(cmd.Cmd):
    def __init__(self, main):
        cmd.Cmd.__init__(self)
        self.main = main
        self.cmdloop()

    def do_navagate(self, t):
        pass
    
    def do_save(self,t):
        pass
    def do_search(self,t):
        

  
Main()