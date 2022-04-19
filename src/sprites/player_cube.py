import os
import pygame

dirname = os.path.dirname(__file__)

class PlayerCube(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0): # pylint: disable=invalid-name
        super().__init__()

        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "red.png"))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
