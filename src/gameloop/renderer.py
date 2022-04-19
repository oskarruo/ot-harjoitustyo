import pygame

class Renderer:
    def __init__(self, display, level):
        self.display = display
        self.level = level

    def render(self):
        self.level.all_sprites.draw(self.display)
        pygame.display.update()
