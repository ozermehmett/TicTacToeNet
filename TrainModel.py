import random
from model import create_model, train_model

model = create_model()

game_counter = 1
modes = ['Easy', 'Hard']

while game_counter <= 20000:
    selected_mode = random.choice(modes)
    model, y, result = train_model(model, selected_mode, print_progress=False, verbose=0)

    if game_counter % 5 == 0:
        print(f'Game: #{game_counter}: result: {result}')
        print(f'Game mode: {selected_mode}')
        print()

    game_counter += 1

model.save('model/tictactoe_model.h5')
