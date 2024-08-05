import random
import numpy as np
from utils import move_generator


def row_win_move_check(current_board_state, available_moves, active_player):
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = active_player

        for i in range(current_board_state_copy.shape[0]):
            if 0 not in current_board_state_copy[i, :] and len(set(current_board_state_copy[i, :])) == 1:
                return coord


def col_win_move_check(current_board_state, available_moves, active_player):
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = active_player

        for i in range(current_board_state_copy.shape[1]):
            if 0 not in current_board_state_copy[:, i] and len(set(current_board_state_copy[:, i])) == 1:
                return coord


def diagonal_win_move_check(current_board_state, available_moves, active_player):
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = active_player

        if 0 not in np.diagonal(current_board_state_copy) and len(set(np.diagonal(current_board_state_copy))) == 1:
            return coord


def diagonal_left2right_win_move_check(current_board_state, available_moves, active_player):
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = active_player

        if 0 not in np.diagonal(np.fliplr(current_board_state_copy)) and len(set(np.diagonal(np.fliplr(current_board_state_copy)))) == 1:
            return coord


def row_blocked_move_check(current_board_state, available_moves, active_player):
    opponent = 1 if active_player == 2 else 2
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = opponent

        for i in range(current_board_state_copy.shape[0]):
            if 0 not in current_board_state_copy[i, :] and (current_board_state_copy[i, :] == opponent).sum() == 2:
                return coord


def col_blocked_move_check(current_board_state, available_moves, active_player):
    opponent = 1 if active_player == 2 else 2
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = opponent

        for i in range(current_board_state_copy.shape[1]):
            if 0 not in current_board_state_copy[:, i] and (current_board_state_copy[:, i] == opponent).sum() == 2:
                return coord


def diagonal_blocked_move_check(current_board_state, available_moves, active_player):
    opponent = 1 if active_player == 2 else 2
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = opponent

        if 0 not in np.diagonal(current_board_state_copy) and (np.diagonal(current_board_state_copy) == opponent).sum() == 2:
            return coord


def diagonal_left2right_blocked_move_check(current_board_state, available_moves, active_player):
    opponent = 1 if active_player == 2 else 2
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = opponent

        if 0 not in np.diagonal(np.fliplr(current_board_state_copy)) and (np.diagonal(np.fliplr(current_board_state_copy)) == opponent).sum() == 2:
            return coord


def row_second_move_check(current_board_state, available_moves, active_player):
    opponent = 1 if active_player == 2 else 2
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = opponent

        for i in range(current_board_state_copy.shape[0]):
            if (current_board_state_copy[i, :] == opponent).sum() == 2 and (current_board_state_copy[i, :] == 0).sum() == 1:
                return coord


def col_second_move_check(current_board_state, available_moves, active_player):
    opponent = 1 if active_player == 2 else 2
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = opponent

        for i in range(current_board_state_copy.shape[1]):
            if (current_board_state_copy[:, i] == opponent).sum() == 2 and (current_board_state_copy[:, i] == 0).sum() == 1:
                return coord


def diagonal_second_move_check(current_board_state, available_moves, active_player):
    opponent = 1 if active_player == 2 else 2
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = opponent

        if (np.diagonal(current_board_state_copy) == opponent).sum() == 2 and (np.diagonal(current_board_state_copy) == 0).sum() == 1:
            return coord


def diagonal_left2right_second_move_check(current_board_state, available_moves, active_player):
    opponent = 1 if active_player == 2 else 2
    available_moves_coord = list(available_moves.keys())
    random.shuffle(available_moves_coord)

    for coord in available_moves_coord:
        current_board_state_copy = current_board_state.copy()
        current_board_state_copy[coord] = opponent

        if (np.diagonal(np.fliplr(current_board_state_copy)) == opponent).sum() == 2 and (np.diagonal(np.fliplr(current_board_state_copy)) == 0).sum() == 1:
            return coord


def opponent_move_selector(current_board_state, active_player, mode):
    available_moves = move_generator(current_board_state, active_player)

    winning_move_checks = [row_win_move_check, col_win_move_check,
                           diagonal_win_move_check, diagonal_left2right_win_move_check]

    blocked_move_checks = [row_blocked_move_check, col_blocked_move_check,
                           diagonal_blocked_move_check, diagonal_second_move_check]

    second_move_checks = [row_second_move_check, col_second_move_check,
                          diagonal_second_move_check, diagonal_left2right_second_move_check]

    if mode == 'Easy':
        return random.choice(list(available_moves.keys()))

    elif mode == 'Hard':
        random.shuffle(winning_move_checks)
        random.shuffle(blocked_move_checks)
        random.shuffle(second_move_checks)

        for fn in winning_move_checks:
            move = fn(current_board_state, available_moves, active_player)
            if move:
                return move

        for fn in blocked_move_checks:
            move = fn(current_board_state, available_moves, active_player)
            if move:
                return move

        for fn in second_move_checks:
            move = fn(current_board_state, available_moves, active_player)
            if move:
                return move

        return random.choice(list(available_moves.keys()))
