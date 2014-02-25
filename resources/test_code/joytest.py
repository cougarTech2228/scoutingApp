# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:43:04 2014

@author: team2228
"""

import pygame
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()
print(j)
while True:
     for evt in pygame.event.get():
         print(evt)
         if evt.type == 10:
            print ("joystick button press")
              
                ##if echoOn and not command:
                ##print("joystick: %s ---Button: %s  " % (evt.joy, evt.button))
                # ^possible later functionality echo^
                
