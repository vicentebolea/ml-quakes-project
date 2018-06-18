from model_factory import ModelFactory
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, Embedding, Activation, Lambda, Bidirectional


class ModelLocation(ModelFactory):
    def create(self):
        model = Sequential()
        model.add(Dense(53, init='normal', input_shape=(self.dim,), activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(5, activation='relu'))
        model.add(Dense(2, init='normal')) #, activation='elu'))
        self.model = model
        return model

