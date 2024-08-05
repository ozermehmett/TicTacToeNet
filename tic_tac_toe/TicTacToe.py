import numpy as np


class TicTacToe(object):
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.activePlayer = 1

    def move(self, player, coord):
        if self.board[coord] != 0 or self.activePlayer != player or self.gameStatus() != 'In progress':
            raise ValueError("Invalid move!")
        self.board[coord] = player
        self.activePlayer = 1 if self.activePlayer == 2 else 2

        return self.gameStatus(), self.board

    def gameStatus(self):
        for i in range(self.board.shape[0]):
            if 0 not in self.board[i, :] and len(set(self.board[i, :])) == 1:
                return 'Win'

        for j in range(self.board.shape[1]):
            if 0 not in self.board[:, j] and len(set(self.board[:, j])) == 1:
                return 'Win'

        if 0 not in np.diagonal(self.board) and len(set(np.diagonal(self.board))) == 1:
            return 'Win'

        if 0 not in np.diagonal(np.fliplr(self.board)) and len(set(np.diagonal(np.fliplr(self.board)))) == 1:
            return 'Win'

        if 0 not in self.board:
            return 'Draw'

        return 'In progress'
