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
        self.comp = input("which competition>>>")
        self.load(self.comp)
        self.data = Data(self.competition, self.robots)
        cmdr(self).cmdloop()

        
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
                
    def reloadSave(self):
        self.load(self.comp)
        self.data.__init__(self.competition)
                
class Data():
    def __init__(self, comp,robos):
        self.competition = comp
        self.robots =robos
        self.roboLists=dict()
        
    def printRD(self, robos):
        if robos == None:
            robos = list(self.robots.keys())
            
        for rn in robos:
            print(rn)
            try:
                robot = self.robots[rn]
                for m in robot.matches:
                    print(m.match, m.alliance)
                    for key in list(m.records.keys()):
                        print("    ",key," - ", m.records[key])

            except KeyError:
                print("no such robot exists")

    '''
    def printAll(self):
        for m in self.competition:
            print (m.number)
            if m.notRun: print("*")
            for n in m.robots:
                r = m.robots[n]
                print ("    ",n)
                try:
                    keys = r.records.keys()
                
                except AttributeError:
                    keys = []
                    
                #print(keys)
                #print(list(keys))
                for k in keys:
                    f = r.records.records[k][0]
                    s = r.records.records[k][1]
                    a = f + s
                    print ("        ",k," attempted-",a," failures-",f," successes-",s)
    '''
    def printMD(self, matches = None , info = True):
        if not matches:
            matches = range(len(self.competition)+1)
            
        for m in [self.competition[n-1] for n in matches]:
            print ("match",m.number)
            try:
                if m.notRun:
                    print("*")
            except:
                print("***")
            robos = m.robots
            for r in list(robos.keys()):
                print("    ",robos[r].teamNumber)
                if info:
                    keys = list(robos[r].records.keys())
                    for k in keys:
                        print(k," - ",robos[r].records[k])
                        
    def simplePrintMD(self, match):
        info= True
        try:
            match = int(match)
            m = self.competition[match-1]
        except:
            print("failed to print match ", match, " invalid or out of range")
            
        print ("match",m.number)
        try:
            if m.notRun:
                print("*")
        except:
            print("***")
        robos = m.robots
        for r in list(robos.keys()):
            print("    ",robos[r].teamNumber)
            if info:
                keys = list(robos[r].records.keys())
                for k in keys:
                    print(k," - ",robos[r].records[k])
               
       
class cmdr(cmd.Cmd):
    def __init__(self, main):
        cmd.Cmd.__init__(self)
        self.data = main.data
        self.level = 1
        self.matches = []
        self.robots = []
        self.dats = []
        
    def do_edit():
        import pdb; pdb.set_trace()
                
    def do_robot(self,line):
        l = line.split()
        
        if "-l" in l[0]:
            try:
                self.data.printRD(self.data.robotLists[l[1]])
            
            except KeyError:
                print("invalid list")
                
        else:
            try:
                robots=[]
                l.pop(0)
                for i in l:
                    robots.append(int(i))
                
                self.data.printRD(robos = robots)
                
            except:
                print("invalid input")
                
    def do_match(self,line):
    
        l = line.split()
        l.pop(0)
        try:
            l[0]
        except:
            print("invalid")
            return
            
        if "-a" in l[0]:
            self.data.printMD()
            
        elif "-l" in l[0]:
            try:
                self.data.printMD(self.data.robotLists[l[1]])
        
            except KeyError:
                print("invalid list")
            except IndexError:
                print("invalid input")
                
        elif "-r" in l[0]:
            try:
                mmin = int(l[1])
                mmax = int(l[2])
                if mmin > mmax:
                    t = mmin
                    mmin = mmax
                    mmax = t
                mmax +=1 
                    
                self.data.printMD(range(mmin , mmax))
                
            except:
                print("invalid input")
        else:
            for m in l:
                self.data.printMD(int(m))
        
    def do_clist(self, line):
        try:
            l[3]
        except:
            print("invalid input")
            return
            
        l = line.split()
        l.pop(0)
        name = l.pop(0)
        r=[]
        for n in l:
            try:
                r.append(int[n])
            except:
                print("must be numbers")
                
        self.data.robotLists[name]=r    

            
    def do_plist(self, line):
        print(self.data.robotLists)
            
    def do_test(self):
        self.data.printAll()
    '''
    def do_showMD(self,t):
        if "-l" in t:
            self.data.printMD(level = 3)
        elif "-s" in t:
            self.data.printMD(level = 1)
        else:
            self.data.printMD()
    '''
    def do_save(self,t):
        self.main.data.save()
        
        
    def do_reload(self, line):
        self.main.data.reloadSave
    '''
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