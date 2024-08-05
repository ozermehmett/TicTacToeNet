from tic_tac_toe import TicTacToe
from utils import move_selector
import keras

model = keras.models.load_model('model/tictactoe_model.h5')

game = TicTacToe()


def print_board(board):
    print()
    for row in board:
        print(' | '.join([' ' if cell == 0 else 'X' if cell == 1 else 'O' for cell in row]))
        print('-' * 9)
    print()


def get_user_move():
    while True:
        try:
            move = input('Enter your move as row,col (e.g., 1,2): ')
            row, col = map(int, move.split(','))
            row, col = row - 1, col - 1
            if row in range(3) and col in range(3) and game.board[row, col] == 0:
                return (row, col)
            else:
                print('Invalid move. Try again.')
        except ValueError:
            print('Invalid input format. Enter row,col as two integers separated by a comma.')


def play_game():
    while game.gameStatus() == 'In progress':
        if game.activePlayer == 1:
            selected_move, new_board_state, _ = move_selector(model, game.board, game.activePlayer)
            game_status, board = game.move(game.activePlayer, selected_move)
            print('AI move:', (selected_move[0] + 1, selected_move[1] + 1))
            print_board(board)

        elif game.activePlayer == 2:
            print('Your turn.')
            user_move = get_user_move()
            game_status, board = game.move(game.activePlayer, user_move)
            print('Opponent move:')
            print_board(board)

        if game.gameStatus() != 'In progress':
            break

    game_status = game.gameStatus()
    if game_status == 'Win':
        winner = 'AI' if game.activePlayer == 2 else 'You'
        result = f'{winner} wins!'
    elif game_status == 'Draw':
        result = 'It\'s a draw!'
    else:
        result = 'Game is incomplete.'

    print(f'Game Over: {result}')


play_game()
