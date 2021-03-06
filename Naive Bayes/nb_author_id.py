#!/usr/bin/python

""" 
    Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

nb_clf = GaussianNB()
# Training the classifier with the training data
t = time()
nb_clf.fit(features_train, labels_train)
print "Time to train: ", round(time() - t, 3)

t1 = time()
pred = nb_clf.predict(features_test)
print "Time to predict: ", round(time() - t1, 3)

X = features_train
Y = labels_train
accuracy = nb_clf.score(X,Y)
print accuracy

acc = accuracy_score(pred, labels_test)
print(acc)
'''
The answer came out to be: 
    no. of Chris training emails:7936
    no. of Sara training emails:7884
    Time to train:  2.004
    Time to predict:  0.331
    0.9786978508217447
    0.9732650739476678
    
'''
#########################################################


