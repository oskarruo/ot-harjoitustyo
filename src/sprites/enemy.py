import os
import pygame

DIR_NAME = os.path.dirname(__file__)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, speed_x=0, speed_y=0): # pylint: disable=invalid-name
        super().__init__()

        self.image = pygame.image.load(os.path.join(DIR_NAME, "..", "assets", "redball.png"))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.speed_x = speed_x
        self.speed_y = speed_y

class RectEnemy(Enemy):
    def __init__(self, width, height, speed, x=0, y=0):
        super().__init__(x, y)
        self.width = width * 30
        self.height = height * 30
        self.speed = speed
        self.lateral = False

        self.height_moved = 0
        self.width_moved = 0
