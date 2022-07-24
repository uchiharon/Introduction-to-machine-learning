#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import time

clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

print("The model accurcy is ", accuracy_score(labels_test,pred))
print("This is the model confusion matrix:", confusion_matrix(labels_test,pred))

for n in range(1,3):
    start = time.time()
    clf1 = KNeighborsClassifier(n_neighbors=7, p=n)
    clf1.fit(features_train, labels_train)
    pred = clf1.predict(features_test)
    print("The accuracy of p= \"{}\" model accurcy is ".format(n), accuracy_score(labels_test,pred), "Its took ", time.time() - start, " to finish") 
    


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
