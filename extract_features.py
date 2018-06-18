import numpy as np
import pandas as pd
import scipy.io as sio
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.feature_extraction import FeatureHasher
from sklearn.cross_validation import train_test_split

FILE1 = './dataset/NN_test_X.mat'
FILE2 = './dataset/NN_test_X_1statn.mat'
FILE3 = './dataset/NN_test_X_3statns.mat'


def prepare_features(labels_file, filekey):
    dataset_x = sio.loadmat(FILE1)['data']
    extra1 = sio.loadmat(FILE2)['data_1statn']
    extra2 = sio.loadmat(FILE3)['data_3statns']

    dataset_x = np.hstack((dataset_x, extra1))
    dataset_x = np.hstack((dataset_x, extra2))
    dataset_y = sio.loadmat(labels_file)[filekey]

    train_x, test_x, train_y, test_y = train_test_split(dataset_x, dataset_y, test_size=0.2)

    return train_x, train_y, test_x, test_y
