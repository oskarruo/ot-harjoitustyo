import unittest
import pygame

from level import Level
from gameloop.gameloop import GameLoop

class StubClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        0

class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key

class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events

class StubRenderer:
    def render(self):
        pass

level_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 5, 3, 0, 0, 0, 8, 3, 1],
            [1, 0, 0, 5, 0, 0, 0, 3, 1],
            [1, 0, 0, 1, 0, 7, 0, 3, 1],
            [1, 2, 0, 0, 0, 0, 0, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]

enemy_info = {"7": [1, 1, 0], "8": [2, 1, 1, 1]}

cellsize = 30

pickup_amount = 0

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level = Level(level_map, cellsize, pickup_amount, enemy_info)
    
    def test_can_complete_level(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_RIGHT)]
    
        gameloop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), cellsize)

        gameloop.start()

        self.assertTrue(self.level.is_finished())
    
    def test_can_fail_level(self):
        events = [StubEvent(pygame.KEYDOWN, pygame.K_UP)]

        gameloop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock(), cellsize)

        gameloop.start()

        self.assertTrue(self.level.check_enemy_collisions())
