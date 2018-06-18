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
    dataset_y = sio.loadmat(labels_file)[filekey]

    train_x, test_x, train_y, test_y = train_test_split(dataset_x, dataset_y, test_size=0.4)

    return train_x, train_y, test_x, test_y
