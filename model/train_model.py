from tic_tac_toe import TicTacToe
from utils import move_selector, opponent_move_selector, unison_shuffled_copies
import numpy as np
from scipy.ndimage import shift


def train_model(model, mode, epochs=1, batch_size=1, print_progress=False, verbose=0):
    if print_progress:
        print('*****************************')
        print('Training model\n')

    game = TicTacToe()
    score_list = []
    corrected_score_list = []
    new_board_state_list = []
    game_status = ''
    result = ''

    while True:
        if game.gameStatus() == 'In progress' and game.activePlayer == 1:
            selected_move, new_board_state, score = move_selector(model, game.board, game.activePlayer)
            score_list.append(score[0][0])
            new_board_state_list.append(new_board_state)

            game_status, board = game.move(game.activePlayer, selected_move)

            if print_progress:
                print('Player 1 move')
                print(board)
                print()

        elif game.gameStatus() == 'In progress' and game.activePlayer == 2:
            selected_move = opponent_move_selector(game.board, game.activePlayer, mode)
            game_status, board = game.move(game.activePlayer, selected_move)

            if print_progress:
                print('Player 2 move')
                print(board)
                print()

        else:
            break

    new_board_state_list = np.array(new_board_state_list)
    new_board_state = new_board_state_list.reshape(-1, 9)

    if game_status == 'Win' and (1 - game.activePlayer) == 1:
        corrected_score_list = shift(score_list, -1, cval=1.0)
        result = 'Win'

    elif game_status == 'Win' and (1 - game.activePlayer) != 1:
        corrected_score_list = shift(score_list, -1, cval=-1.0)
        result = 'Lost'

    elif game_status == 'Draw':
        corrected_score_list = shift(score_list, -1, cval=0.0)
        result = 'Draw'

    if print_progress:
        print('AI:', result)
        print('*****************************\n')

    x, y = unison_shuffled_copies(new_board_state, corrected_score_list)
    x = x.reshape(-1, 9)
    y = np.array(y).reshape(-1, 1)

    model.fit(x, y, epochs=epochs, batch_size=batch_size, verbose=verbose)

    return model, y, result
