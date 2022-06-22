"""
File: BYO_scikitlearn_model
"""
#import all the libraries you need
import argparse
import os
from sklearn.externals import joblib
#TODO add your other required libraries

#functions used in your code


# -TODO-Dictionary to encode labels to codes




# Dictionary to convert codes to labels



#training script
if __name__ =='__main__':
     #------------------------------- parsing input parameters (from command line)
    print('extracting arguments')
    parser = argparse.ArgumentParser()
       
   #TODO: RandomForest hyperparameters



   # TODO: Data, model, and output directories

    
    
    
    
    args = parser.parse_args()
    

    #TODO-Load your data (both training and test) from container filesystem into training / test data sets and split them to train/test features and lables
    
    
     
    #TODO- fit the randomforest model
   

    #Save the model to the location specified by args.model_dir, using the joblib
    


    
    
    
#define a function that loads the model    



#define a custom output function that takes the prediction and changes the numeric labels to the string lables (bonus!)

