#!/usr/bin/env python
from model_factory_method import model_create
from extract_features import prepare_features
from IPython import embed
from os import environ

tests = [
["model_time",       "./dataset/NN_test_Y_ADO.mat", "sWave_ADO"], 
#["model_time",       "./dataset/NN_test_Y_RPV.mat", "sWave_RPV"],
#["model_time",       "./dataset/NN_test_Y_USC.mat", "sWave_USC"],
#["model_time",       "./dataset/NN_test_Y_RSS.mat", "sWave_RSS"],
#["model_depth",      "./dataset/NN_test_Y_depth.mat", "data_depth"],
#["model_location",   "./dataset/NN_test_Y_eqLoc.mat", "data_eqLoc"],
#["model_magnitude",  "./dataset/NN_test_Y_magnitude.mat", "data_mag"]
]

BATCH_SIZE = 1000

EPOCHS     = 2000
if 'EPOCHS' in environ:
    EPOCHS = int(environ['EPOCHS'])


for setup in tests:
    train_x, train_y, test_x, test_y = prepare_features(setup[1], setup[2])
    model_factory = model_create(setup[0],53)
    model = model_factory.model

    #embed()

    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

    model.fit(train_x, train_y,
              batch_size=BATCH_SIZE,
              shuffle=True,
              nb_epoch=EPOCHS,
              verbose=1,
              validation_data=(test_x, test_y))

    score = model.evaluate(test_x, test_y, verbose=0)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

embed()
