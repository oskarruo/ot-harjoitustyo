import pygame
from sprites.PlayerCube import PlayerCube
from sprites.Floor import Floor
from sprites.Wall import Wall
from sprites.Goal import Goal
from sprites.pickup import Pickup

class Level:
    def __init__(self, level_map, cell_size, pickup_amount):
        self.cell_size = cell_size
        self.cube = pygame.sprite.Sprite
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.goaltiles = pygame.sprite.Group()
        self.pickups = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.pickup_amount = pickup_amount
        self.pickups_collected = 0

        self.init_sprites(level_map)

    def init_sprites(self, level_map):
        height =  len(level_map)
        width = len(level_map[0])

        for y in range(height):
            for x in range(width):
                cell = level_map[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif cell == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif cell == 2:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.cube = PlayerCube(normalized_x + 5, normalized_y + 5)
                elif cell == 3:
                    self.goaltiles.add(Goal(normalized_x, normalized_y))
                elif cell == 4:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.pickups.add(Pickup(normalized_x + 7.5, normalized_y + 7.5))

        self.all_sprites.add(self.floors, self.walls, self.goaltiles, self.pickups, self.cube)
    
    def move_cube(self, dx=0, dy=0):
        if self.pickup_collect():
            self.pickups_collected += 1
        if self.goal_reached() and self.finish_allowed():
            return True
        elif not self.move_allowed(dx, dy): 
            self.cube.rect.move_ip(dx, dy)
    
    def move_allowed(self, dx=0, dy=0):
        self.cube.rect.move_ip(dx, dy)
        collision = pygame.sprite.spritecollide(self.cube, self.walls, False)
        self.cube.rect.move_ip(-dx, -dy)
        return collision
    
    def goal_reached(self):
        return pygame.sprite.spritecollide(self.cube, self.goaltiles, False)
    
    def pickup_collect(self):
        return pygame.sprite.spritecollide(self.cube, self.pickups, True)
    
    def finish_allowed(self):
        if self.pickups_collected >= self.pickup_amount:
            return True
        else:
            return False
