# main module
import pygame
from pygame.locals import *

import user
import data
import joy

pygame.init()
pygame.event.set_allowed(10)
joy.joystick_init(True)
