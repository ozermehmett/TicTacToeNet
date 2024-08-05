import unittest
import numpy as np
from utils import move_generator, move_selector
from model import create_model


class TestMoves(unittest.TestCase):

    def setUp(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.model = create_model()

    def test_move_generator(self):
        moves = move_generator(self.board, 1)
        self.assertEqual(len(moves), 9)
        self.assertIn((0, 0), moves)
        self.assertIn((2, 2), moves)

    def test_move_selector(self):
        move, new_board, score = move_selector(self.model, self.board, 1)
        self.assertIn(move, [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
        self.assertEqual(len(new_board), 9)


if __name__ == '__main__':
    unittest.main()
