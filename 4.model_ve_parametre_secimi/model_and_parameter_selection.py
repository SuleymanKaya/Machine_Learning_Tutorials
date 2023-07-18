# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:17:59 2019

@author: suleyman.kaya
"""

import pandas as pd

veriler= pd.read_csv("Social_Network_Ads.csv")
x= veriler.iloc[:,2:4].values
y= veriler.iloc[:,4].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.75, random_state=0)

from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
x_train= sc.fit_transform(x_train)
x_test= sc.transform(x_test)

from sklearn.svm import SVC
classifier= SVC(kernel="rbf", random_state=0)
classifier.fit(x_train, y_train)
y_pred= classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.model_selection import cross_val_score 
svm_basari= cross_val_score(estimator= classifier, X= x_train, y= y_train, cv=4)
print(svm_basari.mean())
print(svm_basari.std())

from sklearn.model_selection import GridSearchCV
p= [{"C":[1,2,3,4,5,6,7], "kernel":["linear"]},
     {"C":[1,10,100,100], "kernel":["rbf"],"gamma":[1,2,0.7,0.07,7, 70, 700]}]
gs= GridSearchCV(estimator=classifier,param_grid= p, scoring="accuracy", cv=4, n_jobs=-1)

grid_search= gs.fit(x_train, y_train)
eniyisonuc= grid_search.best_score_
eniyiparametre= grid_search.best_params_
print(eniyisonuc)
print(eniyiparametre)
