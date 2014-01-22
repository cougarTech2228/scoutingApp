#gui module
#Let's do some work

import pygame

class Gui:
    def __init__(self):
            
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 24)

    # Initiates the match window
    def draw(self): # this should eventually have options 
                    #for window start size placement etc.

        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption('CATS: CougarTech Scouting Application')
        
    def clear(self):
        self.screen.fill((0,0,0))

class Screen():
    pass

class Label():
    def __init__(self, message, size, surface):
        self.font = pygame.font.Font(None,24)
        
        self.X = size[0]
        self.Y = size[1]
        self.message = message
        self.value = 0
        self.color = (255, 255, 255) #white

        self.parent_surface = surface

    def setValue(value):
        self.value = value

    def draw(self, position):
        text = self.font.render(self.message + str(self.value), True, self.color)
        self.parent_surface.blit( text, position)

class List():
    def __init__(self):
        self.entries = []

class Tab():
    pass

