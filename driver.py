#!/usr/bin/env python
from extract_features import *
from model_factory import model_create
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, Embedding, Activation, Lambda, Bidirectional
from keras.layers.recurrent import LSTM, GRU
from keras.optimizers import SGD
from keras import backend as K

tests = [
["model_time",       "./dataset/NN_test_Y_ADO.mat"],
["model_time",       "./dataset/NN_test_Y_ADO.mat"],
["model_time",       "./dataset/NN_test_Y_ADO.mat"],
["model_time",       "./dataset/NN_test_Y_ADO.mat"],
["model_depth",      "./dataset/NN_test_Y_depth.mat"],
["model_location",   "./dataset/NN_test_Y_eqLoc.mat"],
["model_magnitude",  "./dataset/NN_test_Y_magnitude.mat"]
]

for model in tests:
    train_x, train_y, test_x, test_y = feature_extract(model[1])
    model = model_create(model[0])
    

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    model.fit(train_x, train_y,
              batch_size=batch_size,
              shuffle=True,
              epochs=20,
              verbose=1,
              validation_data=(test_x, test_y))

    score = model.evaluate(test_x, test_y, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    model.train(train_x, train_y)
    model.test(test_x, test_y)
