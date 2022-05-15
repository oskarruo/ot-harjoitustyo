import unittest
from level import Level

level_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 4, 3, 0, 0, 0, 8, 3, 1],
            [1, 0, 0, 5, 0, 0, 0, 3, 1],
            [1, 0, 0, 1, 0, 7, 0, 3, 1],
            [1, 2, 0, 0, 0, 0, 0, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]

level_map2 = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 4, 3, 0, 0, 0, 8, 3, 1],
            [1, 0, 0, 5, 0, 0, 0, 3, 1],
            [1, 0, 0, 1, 0, 7, 0, 3, 1],
            [1, 6, 0, 0, 0, 0, 0, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]

enemy_info = {"7": [1, 1, 0], "8": [2, 1, 1, 1]}

cellsize = 30

pickup_amount = 1

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(level_map, cellsize, pickup_amount, enemy_info)

    def assert_coordinates_equal(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_can_move_cube(self):
        cube = self.level.cube
        
        self.assert_coordinates_equal(cube, 1 * cellsize + 5, 4 * cellsize + 5)

        self.level.move_cube(dx=+cellsize)
        self.assert_coordinates_equal(cube, 2 * cellsize + 5, 4 * cellsize + 5)

        self.level.move_cube(dx=-cellsize)
        self.assert_coordinates_equal(cube, 1 * cellsize + 5, 4 * cellsize + 5)
        
        self.level.move_cube(dy=-cellsize)
        self.assert_coordinates_equal(cube, 1 * cellsize + 5, 3 * cellsize + 5)
        
        self.level.move_cube(dy=+cellsize)
        self.assert_coordinates_equal(cube, 1 * cellsize + 5, 4 * cellsize + 5)

    def test_can_not_move_out_of_bounds(self):
        cube = self.level.cube
        self.level.move_cube(dx=-cellsize)
        self.assert_coordinates_equal(cube, 1 * cellsize + 5, 4 * cellsize + 5)
        self.level.move_cube(dy=cellsize)
        self.assert_coordinates_equal(cube, 1 * cellsize + 5, 4 * cellsize + 5)

    def test_can_pick_up_pickups(self):
        self.level.move_cube(dy=-cellsize * 3)
        self.level.pickup_collect()
        self.level.move_cube(dy=cellsize)
        self.assertEqual(self.level.pickups_collected, 1)
    
    def test_finish_not_allowed_when_no_pickups_collected(self):
        self.level.move_cube(dx=cellsize * 6)
        self.assertEqual(self.level.finish_allowed(), False)
        self.assertEqual(self.level.is_finished(), False)
    
    def test_finish_works_when_pickups_collected(self):
        self.level.move_cube(dy=-cellsize * 3)
        self.level.pickup_collect()
        self.level.move_cube(dx=cellsize * 1)
        self.assertEqual(self.level.finish_allowed(), True)
    
    def test_finished_level_ends(self):
        self.level.move_cube(dy=-cellsize * 3)
        self.level.pickup_collect()
        self.level.move_cube(dx=cellsize)
        self.assertEqual(self.level.is_finished(), True)

    def test_enemies_update(self):
        for i in range(10):
            self.level.update_enemies()

    def test_spawn_and_goal_block(self):
        self.level2 = Level(level_map2, cellsize, pickup_amount, enemy_info)
        self.level2.move_cube(dy=-cellsize * 3)
        self.level2.pickup_collect()
        self.level2.move_cube(dy=cellsize * 3)
        self.assertEqual(self.level2.is_finished(), True)
