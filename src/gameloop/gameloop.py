import pygame

class GameLoop:
    def __init__(self, level, renderer, eventqueue, clock, cell_size):
        self.level = level
        self.cell_size = cell_size
        self.renderer = renderer
        self.eventqueue = eventqueue
        self.clock = clock
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def start(self):
        while True:
            if self.eventhandler():
                return
            self.render()
            self.clock.tick(60)
    
    def eventhandler(self):
        for event in self.eventqueue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.right = True
                if event.key == pygame.K_LEFT:
                    self.left = True
                if event.key == pygame.K_UP:
                    self.up = True
                if event.key == pygame.K_DOWN:
                    self.down = True
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.right = False
                if event.key == pygame.K_LEFT:
                    self.left = False
                if event.key == pygame.K_UP:
                    self.up = False
                if event.key == pygame.K_DOWN:
                    self.down = False     

            if event.type == pygame.QUIT:
                exit()
        
        if self.right:
            if self.level.move_cube(dx=2):
                return True
        if self.left:
            if self.level.move_cube(dx=-2):
                return True
        if self.up:
            if self.level.move_cube(dy=-2):
                return True
        if self.down:
            if self.level.move_cube(dy=2):
                return True
        
    def render(self):
        self.renderer.render()
