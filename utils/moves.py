def move_generator(current_board_state, active_player):
    available_moves = {}
    for row in range(current_board_state.shape[0]):
        for col in range(current_board_state.shape[1]):
            if current_board_state[row, col] == 0:
                board_state_copy = current_board_state.copy()
                board_state_copy[row, col] = active_player
                available_moves[(row, col)] = board_state_copy.flatten()

    return available_moves


def move_selector(model, current_board_state, active_player):
    tracker = {}

    available_moves = move_generator(current_board_state, active_player)

    for move_coord in available_moves:
        score = model.predict(available_moves[move_coord].reshape(1, 9))
        tracker[move_coord] = score

    selected_move = max(tracker, key=tracker.get)
    new_board_state = available_moves[selected_move]
    score = tracker[selected_move]

    return selected_move, new_board_state, score
