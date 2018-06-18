from model_factory import ModelFactory
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, Embedding, Activation, Lambda, Bidirectional


class ModelMagnitude(ModelFactory):
    def create(self):
        model = Sequential()
        model.add(Dense(53, init='normal', input_shape=(self.dim,), activation='relu'))
        model.add(Dense(10, activation='relu'))
        model.add(Dense(1, init='normal'))
        self.model = model
        return model
