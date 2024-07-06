You work for a company that has decided to build an AI system for house price prediction. 
To make sure that the model stays relevant over time, it is important to retrain the model with the latest collected data. 
You have been given a task to implement an MLOps (Machine Learning Operations) pipeline in Python for training, evaluating the model performance and deploying the model.
Please write a Python script that takes as input a csv file with housing data, and as output, trains a multiple linear regression model on it using Sklearn, evaluates the model performance using RMSE (Root Mean Square Error) and then saves the trained model to disk. 
Also, write a script to load and use this model to make predictions.
(Remember to replace 'features_column' with the correct column names from your data. The model saving and loading part is a simplistic implementation of model versioning which is a part of MLOps.)


# Requirements
 - Task: house price prediction
 - Method: Linear regression model
 - Tech stack: Python, csv, Sklearn
 - Eval metric: RMSE (Root Mean Square Error)
 - Features: 
    - train models
    - evaluate models
    - save models on disk
    - create: train -> evaluate -> save model; pipeline
    - load (best) model & perform inference
    - adapt to frequent data changes 
    - deploying models 


    
