#gui module

class Gui
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
