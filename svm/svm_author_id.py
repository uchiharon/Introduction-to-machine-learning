#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("E:/uoc/Machine_Learning_Projects-ud120-projects/tools")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###


from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import time

t0 = time.time()
clr = SVC(kernel='rbf', gamma='auto', C=10000)
clr.fit(features_train,labels_train)
print("training time:", round(time.time() - t0, 3), "sec")

t1 = time.time()
preds = clr.predict(features_test)
print("prediction time:", round(time.time() - t1,3), "sec")
print("prediction accuracy:", accuracy_score(preds,labels_test))

#########################################################


