import sys
import pygame

class GameLoop:
    def __init__(self, level, renderer, eventqueue, clock, cell_size):
        self.level = level
        self.cell_size = cell_size
        self.renderer = renderer
        self.eventqueue = eventqueue
        self.clock = clock
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def start(self):
        while True:
            if self.eventhandler():
                return True
            self.level.update_enemies()
            if self.level.check_enemy_collisions():
                return False
            self.render()
            self.clock.tick(60)

    def eventhandler(self):
        for event in self.eventqueue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.move_right = True
                if event.key == pygame.K_LEFT:
                    self.move_left = True
                if event.key == pygame.K_UP:
                    self.move_up = True
                if event.key == pygame.K_DOWN:
                    self.move_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.move_right = False
                if event.key == pygame.K_LEFT:
                    self.move_left = False
                if event.key == pygame.K_UP:
                    self.move_up = False
                if event.key == pygame.K_DOWN:
                    self.move_down = False

            if event.type == pygame.QUIT:
                sys.exit()

        if self.move_right:
            if self.level.move_cube(dx=2):
                return True
        if self.move_left:
            if self.level.move_cube(dx=-2):
                return True
        if self.move_up:
            if self.level.move_cube(dy=-2):
                return True
        if self.move_down:
            if self.level.move_cube(dy=2):
                return True

    def render(self):
        self.renderer.render()
