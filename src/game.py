import pygame
from stagehandler import Stagehandler
from level import Level
from gameloop.clock import Clock
from gameloop.eventqueue import EventQueue
from gameloop.renderer import Renderer
from gameloop.gameloop import GameLoop

class Game: # pylint: disable=too-many-instance-attributes
    """Class for the game.
    Attributes:
        stagehandler: Handles reading stages.json file and current number of stage and returns necessary information
        single_stage: Bool that is True if stage was specifically selected in the UI
        level_map: Array that contains the map of the level
        cellsize: Integer that tells how wide (in px) a single square on the map is
        pickup_amount: Integer that tells how many pickups are to be collected in a stage
        height: Integer that tells the height of the stage in squares
        width: Integer that tells the width of the stage in squares
        display_height: Integer that tells the height of the window in pixels
        display_width: Integer that tells the width of the window in pixels
        display: Sets the display width and height
    """
    def __init__(self, stage=0, single_stage=False): # pylint: disable=too-many-statements
        """Constructor for the class
        Args:
            stage: Specifies the stagenumber if a stage was specifically selected in the UI
            single_stage: Bool that is True if stage was specifically selected in the UI
        """
        self.stagehandler = Stagehandler()
        self.stagehandler.current_stage = stage
        self.single_stage = single_stage
        self.level_map = self.stagehandler.get_stagemap()
        self.cellsize = self.stagehandler.get_stage_cellsize()
        self.pickup_amount = self.stagehandler.get_stage_pickup_amount()
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

        if gameloop.start() is False:
            self.__init__(stage, self.single_stage)

        if self.single_stage or gameloop.quit:
            pygame.quit()
        else:
            self.next_level()

    def next_level(self):
        """Changes the stage to the next one unless the final stage has been completed
        """
        if self.stagehandler.next_stage():
            self.game_complete()
        else:
            self.__init__(self.stagehandler.current_stage)

    def game_complete(self):
        """Exits the game keeping the UI running
        """
        pygame.quit()
