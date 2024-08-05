import keras
from tensorflow.keras.layers import Dense, Input, Dropout


def create_model():
    model = keras.Sequential()
    model.add(Input(shape=(9,)))
    model.add(Dense(units=128, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(units=64, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(units=32, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(units=1, activation='linear'))

    model.compile(loss='mean_squared_error', optimizer='adam')

    return model
