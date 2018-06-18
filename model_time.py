from model_factory import ModelFactory
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, Embedding, Activation, Lambda, Bidirectional


class ModelTime(ModelFactory):
    def create(self):
        self.model = Sequential()
        model = Sequential()
        model.add(Dense(53, input_shape=(self.dim,), activation='relu'))
#        model.add(Dropout(0.25))
        model.add(Dense(25))
        #model.add(Dropout(0.25))
        #model.add(Dense(20))
        #model.add(Dense(10))
        model.add(Dense(1)) #, activation='sigmoid'))
        return model
