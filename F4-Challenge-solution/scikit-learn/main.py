"""
File: BYO_scikitlearn_model
"""

import argparse
import numpy as np
import os
import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Dictionary to encode labels to codes
label_encode = {
    'Iris-virginica': 0,
    'Iris-versicolor': 1,
    'Iris-setosa': 2
}

# Dictionary to convert codes to labels
label_decode = {
    0: 'Iris-virginica',
    1: 'Iris-versicolor',
    2: 'Iris-setosa'
}



if __name__ =='__main__':
    #------------------------------- parsing input parameters (from command line)
    print('extracting arguments')
    parser = argparse.ArgumentParser()
       
   #TODO: RandomForest hyperparameters
    parser.add_argument('--n_estimators', type=int, default=10)
    parser.add_argument('--min_samples_leaf', type=int, default=3)
    
    
   # TODO: Data, model, and output directories
    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--test', type=str, default=os.environ.get('SM_CHANNEL_TEST'))

    args = parser.parse_args()
    
    train = pd.read_csv(os.path.join(args.train,'train.csv'),index_col=0, engine="python")
    y_train= train['label'].map(label_encode)
    X_train =  train.drop(["label"], axis=1)
    
    
    test = pd.read_csv(os.path.join(args.test,'test.csv'),index_col=0, engine="python")
    y_test= test['label'].map(label_encode)
    X_test =  test.drop(["label"], axis=1)
   
        
    #train the randomforest regression model
    model= RandomForestClassifier(
        n_estimators=args.n_estimators,
        min_samples_leaf=args.min_samples_leaf)
    
    model.fit(X_train, y_train)

    #Save the model to the location specified by args.model_dir
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))


def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return model
     
def output_fn(prediction, content_type):
    return ' | '.join([label_decode[t] for t in prediction])