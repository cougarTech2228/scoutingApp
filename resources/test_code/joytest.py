# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:43:04 2014

@author: team2228
"""

import pygame
pygame.init()
pygame.event.set_blocked(7)
pygame.event.set_blocked(11)

for x in range(pygame.joystick.get_count()):
    pygame.joystick.Joystick(x).init()
    print("asdf")

def p():#n is index
    while True:
        print(pygame.event.wait())
        
        



    
                ##if echoOn and not command:
                ##print("joystick: %s ---Button: %s  " % (evt.joy, evt.button))
                # ^possible later functionality echo^
                
