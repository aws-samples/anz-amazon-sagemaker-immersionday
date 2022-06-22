"""
File: BYO_scikitlearn_model
"""

import argparse
import numpy as np
import os
import pandas as pd
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-data-dir', type=str, default=os.environ.get('SM_OUTPUT_DATA_DIR'))
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
   
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.fit_transform(X_test)
    
    #train the logistic regression model
    model = LogisticRegression().fit(X_train, y_train, eval_set=(X_test, y_test), logging_level='Silent')

    #Save the model to the location specified by args.model_dir
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))


def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return model
     
def output_fn(prediction, content_type):
    return ' | '.join([label_decode[t] for t in prediction])