# main module
import pygame
from pygame.locals import *

import user
import data
import joy

RED = 1
BLUE = 2


pygame.init()
pygame.event.set_allowed(10)
<<<<<<< HEAD
joy.joystick_init()
terminalInterface = user.CLI()
=======
joy.joystick_init(True)
>>>>>>> master
