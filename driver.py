#!/usr/bin/env python
import numpy as np
from sklearn import linear_model
from model_factory_method import model_create
from extract_features import prepare_features
from IPython import embed
from os import environ
from sklearn.metrics import accuracy_score, precision_score

tests = [
["model_time",       "./dataset/NN_test_Y_ADO.mat", "sWave_ADO"], 
["model_time",       "./dataset/NN_test_Y_RPV.mat", "sWave_RPV"],
["model_time",       "./dataset/NN_test_Y_USC.mat", "sWave_USC"],
["model_time",       "./dataset/NN_test_Y_RSS.mat", "sWave_RSS"],
["model_depth",      "./dataset/NN_test_Y_depth.mat", "data_depth"],
["model_magnitude",  "./dataset/NN_test_Y_magnitude.mat", "data_mag"],
["model_location",   "./dataset/NN_test_Y_eqLoc.mat", "data_eqLoc"]
]

BATCH_SIZE = 100

EPOCHS     = 2000
if 'EPOCHS' in environ:
    EPOCHS = int(environ['EPOCHS'])


scores = { }
for setup in tests:
    train_x, train_y, test_x, test_y = prepare_features(setup[1], setup[2])
    model_factory = model_create(setup[0],53)
    model = model_factory.model

    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mse','accuracy'])

    model.fit(train_x, train_y,
              batch_size=BATCH_SIZE,
              shuffle=True,
              nb_epoch=EPOCHS,
              verbose=1,
              validation_split=0.2)

    scores[setup[2]] = model.evaluate(test_x, test_y, verbose=0)
    #print('Test loss:', score[0])
    #print('Test mse:', score[1])


for name,score in scores.iteritems():
    print "TEST NAME: ", name
    print "Total MSE: ", score[1]


#embed()
