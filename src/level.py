import pygame
from sprites.player_cube import PlayerCube
from sprites.floor import Floor
from sprites.wall import Wall
from sprites.goal import Goal
from sprites.pickup import Pickup
from sprites.enemy import Enemy

class Level: # pylint: disable=too-many-instance-attributes
    def __init__(self, level_map, cell_size, pickup_amount):
        self.cell_size = cell_size
        self.cube = pygame.sprite.Sprite
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.goaltiles = pygame.sprite.Group()
        self.pickups = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.pickup_amount = pickup_amount
        self.pickups_collected = 0

        self._init_sprites(level_map)

    def _init_sprites(self, level_map): # pylint: disable=too-many-statements
        height = len(level_map)
        width = len(level_map[0])

        for y in range(height): # pylint: disable=invalid-name
            for x in range(width): # pylint: disable=invalid-name
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
                elif cell == 5:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.enemies.add(Enemy(normalized_x + 7.5, normalized_y + 7.5))
                elif cell == 6:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.enemies.add(Enemy(normalized_x + 7.5, normalized_y + 7.5, 4, 0))
                elif cell == 7:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.enemies.add(Enemy(normalized_x + 7.5, normalized_y + 7.5, 0, 4))

        self.all_sprites.add(self.floors, self.walls, self.goaltiles, self.pickups, self.cube, self.enemies)

    def move_cube(self, dx=0, dy=0): # pylint: disable=invalid-name
        if self._pickup_collect():
            self.pickups_collected += 1
        if self._goal_reached() and self._finish_allowed():
            return True
        if not self._move_allowed(dx, dy):
            self.cube.rect.move_ip(dx, dy)

    def _move_allowed(self, dx=0, dy=0): # pylint: disable=invalid-name
        self.cube.rect.move_ip(dx, dy)
        collision = pygame.sprite.spritecollide(self.cube, self.walls, False)
        self.cube.rect.move_ip(-dx, -dy)
        return collision

    def _goal_reached(self):
        return pygame.sprite.spritecollide(self.cube, self.goaltiles, False)

    def _pickup_collect(self):
        return pygame.sprite.spritecollide(self.cube, self.pickups, True)

    def _finish_allowed(self):
        if self.pickups_collected >= self.pickup_amount:
            return True
        return False

    def update_enemies(self):
        for enemy in self.enemies:
            self._enemy_change_dir(enemy)
            enemy.rect.move_ip(enemy.speed_x, enemy.speed_y)

    def _enemy_change_dir(self, enemy):
        if pygame.sprite.spritecollide(enemy, self.walls, False):
            enemy.speed_x = -enemy.speed_x
            enemy.speed_y = -enemy.speed_y

    def check_enemy_collisions(self):
        return pygame.sprite.spritecollide(self.cube, self.enemies, False)
