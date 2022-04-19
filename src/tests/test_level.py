import unittest
from level import Level

level_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 4, 0, 0, 0, 0, 0, 3, 1],
            [1, 0, 0, 5, 0, 1, 0, 3, 1],
            [1, 0, 0, 1, 6, 7, 0, 3, 1],
            [1, 2, 0, 0, 0, 0, 0, 3, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]]

cellsize = 30

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(level_map, cellsize, 1)
    
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
        self.level.move_cube(dy=cellsize)
        self.assertEqual(self.level.pickups_collected, 1)
    
    def test_finish_not_allowed_when_no_pickups_collected(self):
        self.level.move_cube(dx=cellsize * 6)
        self.assertEqual(self.level.finish_allowed(), False)
    
    def test_finish_works_when_pickups_collected(self):
        self.level.move_cube(dy=-cellsize * 3)
        self.level.move_cube(dx=cellsize * 6)
        self.assertEqual(self.level.finish_allowed(), True)
    
    def test_finished_level_ends(self):
        self.level.move_cube(dy=-cellsize * 3)
        self.level.move_cube(dx=cellsize * 6)
        self.assertEqual(self.level.move_cube(), True)
