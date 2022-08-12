#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("E:/uoc/Machine_Learning_Projects-ud120-projects/naive_bayes")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
import numpy as np



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels





#########################################################
### your code goes here ###



def author_prediction(books):
    # Data preparation
    features_train, features_test, labels_train, labels_test, book = preprocess(book = books)
    # Building model
    clr = GaussianNB()
    clr.fit(features_train,labels_train)
    # Making prediction with model
    pred = clr.predict(book)
    if pred == 1:
        result = "Chris"
    else:
        result = "Sara"
        
    return  result



    


#########################################################


