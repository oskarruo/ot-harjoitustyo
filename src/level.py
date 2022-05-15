import pygame
from sprites.player_cube import PlayerCube
from sprites.floor import Floor
from sprites.wall import Wall
from sprites.goal import Goal
from sprites.pickup import Pickup
from sprites.enemy import Enemy, RectEnemy

class Level: # pylint: disable=too-many-instance-attributes
    """Class for the level.
    Attributes:
        cell_size: How wide a square on the map is
        cube: The cube which is controlled by the player
        floors: Tiles which the cube can move on
        walls: Tiles which the cube can not move on
        goaltiles: Tiles where the level will end
        pickups: Items the player has to collect
        enemies: Objects which the player has to avoid
        all_sprites: A sprite group with all of the sprites
        pickup_amount: The amount of pickups needed to complete the level
        enemy_info: Dictionary with information about the enemies in the level
        pickups_collected: How many pickups the player has collected
    """
    def __init__(self, level_map, cell_size, pickup_amount, enemy_info):
        """Constructor for the class
        Args:
            level_map: Array of the stage
            cell_size: How wide a square on the map is
            pickup_amount: How many pickups the stage has
            enemy_info: Information about the enemies
        """
        self.cell_size = cell_size
        self.cube = pygame.sprite.Sprite
        self.floors = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.goaltiles = pygame.sprite.Group()
        self.pickups = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.pickup_amount = pickup_amount
        self.enemy_info = enemy_info
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
                    self.goaltiles.add(Goal(normalized_x, normalized_y))
                    self.cube = PlayerCube(normalized_x + 5, normalized_y + 5)
                elif cell > 6:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    if self.enemy_info[str(cell)][0] == 1:
                        self.enemies.add(Enemy(normalized_x + 7.5, normalized_y + 7.5, self.enemy_info[str(cell)][1], self.enemy_info[str(cell)][2]))
                    if self.enemy_info[str(cell)][0] == 2:
                        self.enemies.add(RectEnemy(self.enemy_info[str(cell)][1], self.enemy_info[str(cell)][2], self.enemy_info[str(cell)][3], normalized_x + 7.5, normalized_y + 7.5))

        self.all_sprites.add(self.floors, self.walls, self.goaltiles, self.pickups, self.cube, self.enemies)

    def move_cube(self, dx=0, dy=0): # pylint: disable=invalid-name
        """Moves the cube in the level if it is allowed
        Args:
            dx: How much the cube moves on the x-axis, default is 0
            dy: How much the cube moves on the y-axis, default is 0
        """
        if not self._move_allowed(dx, dy):
            self.cube.rect.move_ip(dx, dy)

    def _move_allowed(self, dx=0, dy=0): # pylint: disable=invalid-name
        self.cube.rect.move_ip(dx, dy)
        collision = pygame.sprite.spritecollide(self.cube, self.walls, False)
        self.cube.rect.move_ip(-dx, -dy)
        return collision

    def _goal_reached(self):
        return pygame.sprite.spritecollide(self.cube, self.goaltiles, False)

    def pickup_collect(self):
        """Checks if player collides with a pickup and if so, adds 1 to the collected attribute
        """
        if pygame.sprite.spritecollide(self.cube, self.pickups, True):
            self.pickups_collected += 1

    def _finish_allowed(self):
        if self.pickups_collected >= self.pickup_amount:
            return True
        return False

    def is_finished(self):
        """Checks if player has reached goal and has enough pickups to complete the game
        Returns:
            True, if winning conditions are met, else False
        """
        if self._goal_reached() and self._finish_allowed():
            return True
        return False

    def update_enemies(self):
        """Updates the position of enemies in the level
        """
        for enemy in self.enemies:
            self._enemy_change_dir(enemy)
            if isinstance(enemy, RectEnemy):
                if enemy.lateral:
                    enemy.rect.move_ip(enemy.speed, 0)
                    enemy.width_moved += abs(enemy.speed)
                else:
                    enemy.rect.move_ip(0, enemy.speed)
                    enemy.height_moved += abs(enemy.speed)
            else:
                enemy.rect.move_ip(enemy.speed_x, enemy.speed_y)

    def _enemy_change_dir(self, enemy):
        if pygame.sprite.spritecollide(enemy, self.walls, False):
            enemy.speed_x = -enemy.speed_x
            enemy.speed_y = -enemy.speed_y
        if isinstance(enemy, RectEnemy):
            if enemy.height_moved == enemy.height:
                enemy.lateral = True
                enemy.height_moved = 0
                enemy.speed = -enemy.speed
            if enemy.width_moved == enemy.width:
                enemy.lateral = False
                enemy.width_moved = 0

    def check_enemy_collisions(self):
        """Checks if player collides with an enemy
        Returns:
            True, if there is collision, else False
        """
        return pygame.sprite.spritecollide(self.cube, self.enemies, False)
