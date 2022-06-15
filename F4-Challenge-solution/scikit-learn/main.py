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
    #parser.add_argument('--test', type=str, default=os.environ.get('SM_CHANNEL_TEST'))

    args = parser.parse_args()

    data = pd.read_csv(os.path.join(args.train,'data.csv'),index_col=0, engine="python")

    Y_encoded = data['label'].map(label_encode)
    X =  data.drop(["label"], axis=1)

    train_X, test_X, train_y, test_y = train_test_split(X, Y_encoded, test_size=0.2) 
    sc = StandardScaler()
    X_train = sc.fit_transform(train_X)
    X_test = sc.fit_transform(test_X)
    
    #train the logistic regression model
    model = LogisticRegression().fit(X_train, train_y)

    #Save the model to the location specified by args.model_dir
    joblib.dump(model, os.path.join(args.model_dir, "model.joblib"))


def model_fn(model_dir):
    model = joblib.load(os.path.join(model_dir, "model.joblib"))
    return model



def input_fn(request_body, request_content_type):
    if request_content_type == 'text/csv':
        samples = []
        for r in request_body.split('\n'):
            samples.append(list(map(float,r.split(','))))
        return np.array(samples)
    else:
        raise ValueError("This model only supports text/csv input")



def predict_fn(input_data, model):
    return model.predict(input_data)


def output_fn(prediction, content_type):
    return ' | '.join([label_decode[t] for t in prediction])
