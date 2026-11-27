import unittest
from strategy_helpers import bfs_first_step, legal_commands, static_score

class StrategyHelperTests(unittest.TestCase):
    def test_no_reverse(self):
        self.assertNotIn("D", legal_commands("U"))

    def test_bfs_first_step(self):
        self.assertEqual(bfs_first_step((0, 0), (2, 0), lambda x, y: 0 <= x <= 2 and y == 0), "R")

    def test_weighted_cells_and_edge_penalty(self):
        owner = [[0, 0], [0, 0]]
        terrain = [[".", "*"], [".", "."]]
        # Raw 6 points, perimeter 8 edges => penalty 2.
        self.assertEqual(static_score(owner, terrain, 0), 4)

if __name__ == "__main__":
    unittest.main()
