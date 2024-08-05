import unittest
import numpy as np
from tic_tac_toe import TicTacToe
from utils import move_generator


class TestTicTacToe(unittest.TestCase):
    def test_initial_board(self):
        game = TicTacToe()
        np.testing.assert_array_equal(game.board, np.zeros((3, 3), dtype=int))

    def test_move(self):
        game = TicTacToe()
        status, board = game.move(player=1, coord=(0, 0))
        self.assertEqual(status, 'In progress')
        np.testing.assert_array_equal(board[0, 0], 1)

    def test_invalid_move(self):
        game = TicTacToe()
        game.move(player=1, coord=(0, 0))
        with self.assertRaises(ValueError):
            game.move(player=1, coord=(0, 0))

    def test_win_condition(self):
        game = TicTacToe()
        game.move(player=1, coord=(0, 0))
        game.move(player=2, coord=(1, 0))
        game.move(player=1, coord=(0, 1))
        game.move(player=2, coord=(1, 1))
        status, _ = game.move(player=1, coord=(0, 2))
        self.assertEqual(status, 'Win')

    def test_draw_condition(self):
        game = TicTacToe()
        moves = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (1, 2), (2, 1), (2, 0), (2, 2)]
        players = [1, 2, 1, 2, 1, 2, 1, 2, 1]
        for player, move in zip(players, moves):
            game.move(player=player, coord=move)
        self.assertEqual(game.gameStatus(), 'Draw')

    def test_move_generator(self):
        game = TicTacToe()
        moves = move_generator(game.board, game.activePlayer)
        expected_moves = {
            (0, 0): np.array([1, 0, 0, 0, 0, 0, 0, 0, 0]),
            (0, 1): np.array([0, 1, 0, 0, 0, 0, 0, 0, 0]),
            (0, 2): np.array([0, 0, 1, 0, 0, 0, 0, 0, 0]),
            (1, 0): np.array([0, 0, 0, 1, 0, 0, 0, 0, 0]),
            (1, 1): np.array([0, 0, 0, 0, 1, 0, 0, 0, 0]),
            (1, 2): np.array([0, 0, 0, 0, 0, 1, 0, 0, 0]),
            (2, 0): np.array([0, 0, 0, 0, 0, 0, 1, 0, 0]),
            (2, 1): np.array([0, 0, 0, 0, 0, 0, 0, 1, 0]),
            (2, 2): np.array([0, 0, 0, 0, 0, 0, 0, 0, 1]),
        }
        for move, board_state in moves.items():
            np.testing.assert_array_equal(board_state, expected_moves[move])


if __name__ == '__main__':
    unittest.main()
