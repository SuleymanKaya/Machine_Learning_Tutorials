# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:50:47 2019

@author: suleyman.kaya
"""

import pandas as pd

veriler= pd.read_csv("Wine.csv")
x= veriler.iloc[:,0:13].values
y= veriler.iloc[:,13].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, train_size=0.8, random_state=0)

from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
x_train= sc.fit_transform(x_train)
x_test= sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)
y_pred = classifier.predict(x_test)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
lda= LDA(n_components= 2)
x_train2= lda.fit_transform(x_train, y_train)
x_test2= lda.transform(x_test)

classifier.fit(x_train2,y_train)
y_pred2= classifier.predict(x_test2)

from sklearn.metrics import confusion_matrix

cm= confusion_matrix(y_test, y_pred)
print(cm)

cm2= confusion_matrix(y_test, y_pred2)
print(cm2)
