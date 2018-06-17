import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.feature_extraction import FeatureHasher
from vars_local import *

def prepare_features(ds):
    ds  = ds.drop('Tumor_Sample_ID', axis = 1)

  variant_data     = ds.Variant_Type.values;
  gene_name_data   = ds.Gene_Name.values;
  reference_allele = ds.Reference_Allele.values;
  tumor_Allele     = ds.Tumor_Allele.values;
  chromosome       = ds.Chromosome.values;
  start_position   = ds.Start_Position.values;

  ds = ds.drop('Chromosome', axis = 1)
  ds = ds.drop('Gene_Name', axis = 1)
  ds = ds.drop('Variant_Type', axis = 1)
  ds = ds.drop('Reference_Allele', axis = 1)
  ds = ds.drop('Tumor_Allele', axis = 1)

  l_encoder  = LabelEncoder()
  OH_encoder = OneHotEncoder(sparse = False)
  hasher     = FeatureHasher(n_features = 100, input_type = 'string', non_negative=True)

  # Diagnosis values are strings. Changing them into numerical values using LabelEncoder.
  ds = pd.concat([ds, pd.DataFrame(OH_encoder.fit_transform(l_encoder.fit_transform(variant_data).reshape(-1,1)))], 
          axis=1, join_axes=[ds.index])

  ds_chrome = pd.DataFrame(OH_encoder.fit_transform(l_encoder.fit_transform(chromosome).reshape(-1,1)))
  ds = pd.concat([ds, ds_chrome], axis=1, join_axes=[ds.index])

  pos = pd.cut(start_position, bins= START_POSITION_BINS, labels=range(START_POSITION_BINS))

  ds = pd.concat([ds, pd.DataFrame(OH_encoder.fit_transform(np.asarray(pos).reshape(-1,1)))], axis=1, join_axes=[ds.index])
  ds = pd.concat([ds, pd.DataFrame(hasher.transform(gene_name_data).toarray())], axis=1, join_axes=[ds.index])


    dataset_y = ds.pop("Cancer_Type")
    dataset_x = ds 
    train_x , test_x, train_y, test_y = cross_validation.train_test_split(dataset_x, dataset_y, test_size=0.2, 
            random_state=0)

    encoder  = LabelEncoder()
    train_y = encoder.fit_transform(train_y)
    test_y = encoder.fit_transform(test_y)

    return (train_x.as_matrix(), train_y, test_x.as_matrix(), test_y)

(train_x, train_y, test_x, test_y) = load_data()

train_y= keras.utils.to_categorical(train_y, NUM_CLASSES)
test_y = keras.utils.to_categorical(test_y, NUM_CLASSES)
  return ds
