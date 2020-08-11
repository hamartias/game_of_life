import unittest
from game import GameOfLife

class TestGame(unittest.TestCase):
    def test_init(self):
        gt = GameOfLife(0, 0)
        self.assertEqual(gt.grid, [])

        gt = GameOfLife(100, 100)
        self.assertTrue(len(gt.grid) == 100)
        self.assertTrue(len(gt.grid[0]) == 100)

    def test_neighbors(self):
        gt = GameOfLife(10, 10)

        # Try low edge square
        neighbors1 = gt.neighbors(0, 0)
        expected1 = [(1, 0), (0, 1), (1, 1)]
        self.assertTrue(len(neighbors1) == 3)
        self.assertEqual(sorted(neighbors1), sorted(expected1))
        self.assertTrue(len(gt.neighbors(1, 1)) == 8)

        # Try middle square
        neighbors2 = sorted(gt.neighbors(5, 5))
        expected2 = [
            (4, 4), (6, 6),
            (4, 6), (6, 4),
            (4, 5), (5, 4),
            (5, 6), (6, 5)
        ]
        self.assertEqual(neighbors2, sorted(expected2))

        # Try high edge square
        neighbors3 = sorted(gt.neighbors(9, 9))
        expected3 = [(8, 9), (8, 8), (9, 8)]
        self.assertEqual(neighbors3, sorted(expected3))

    def test_update(self):
        gt = GameOfLife(10, 10)
        grid_init = gt.grid.copy()
        gt.update_grid()
        self.assertEqual(grid_init, gt.grid)

        # kill off overpopulated cell
        empty_grid = [[0 for i in range(3)] for j in range(3)]
        gt = GameOfLife(3, 3)
        gt.grid = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
        gt.update_grid()
        self.assertEqual(gt.grid[1][1], 0)

        # bring alive cell with population 3
        gt.grid = [
            [0, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        gt.update_grid()
        self.assertEqual(gt.grid[0][0], 1)

        # kill underpopulated cell
        gt.grid = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        gt.update_grid()
        self.assertEqual(gt.grid, empty_grid)

if __name__=='__main__':
    unittest.main()
