import pygame
from stagehandler import Stagehandler
from level import Level
from gameloop.clock import Clock
from gameloop.eventqueue import EventQueue
from gameloop.renderer import Renderer
from gameloop.gameloop import GameLoop

stagehandler = Stagehandler()

class Game:
    def __init__(self):
        self.level_map = stagehandler.get_stagemap()
        self.cellsize = stagehandler.get_stage_cellsize()
        self.pickup_amount = stagehandler.get_stage_pickup_amount()
        
        self.height = len(self.level_map)
        self.width = len(self.level_map[0])
        self.display_height = self.height * self.cellsize
        self.display_width = self.width * self.cellsize
        self.display = pygame.display.set_mode((self.display_width, self.display_height))

        pygame.display.set_caption("World's Hardest Game")

        level = Level(self.level_map, self.cellsize, self.pickup_amount)
        eventqueue = EventQueue()
        clock = Clock()
        renderer = Renderer(self.display, level)
        gameloop = GameLoop(level, renderer, eventqueue, clock, self.cellsize)
        
        pygame.init()
        gameloop.start()
        self.next_level()

    def next_level(self):
        if stagehandler.next_stage():
            self.game_complete()
        else:
            self.__init__()

    def game_complete(self):
        pygame.init()
        display = pygame.display.set_mode((880, 40))
        font = pygame.font.SysFont("Arial", 24)
        text = font.render("Voitit pelin! Paina ENTER pelataksesi uudestaan tai paina ESC poistuaksesi pelistä.", True, (255, 0, 0))
        display.blit(text, (0, 0))
        pygame.display.flip
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_RETURN:
                        self.restart()

    def restart(self):
        stagehandler.reset_stages()
        self.__init__()            

if __name__ == "__main__":
    Game()
