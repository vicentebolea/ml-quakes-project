from model_factory import ModelFactory
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, Embedding, Activation, Lambda, Bidirectional


class ModelTime(ModelFactory):
    def create(self):
        self.model = Sequential()
        model = Sequential()
        model.add(Dense(78, input_shape=(self.dim,), activation='relu'))
        model.add(Dense(39, activation='relu'))
        model.add(Dense(20, activation='relu'))
        model.add(Dense(1))
        return model
