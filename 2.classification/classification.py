# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:08:34 2019

@author: suleyman.kaya
"""

#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix


veriler=pd.read_csv('veriler.csv')

x= veriler.iloc[:,1:4].values
y= veriler.iloc[:,4:].values


from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(x_train)
X_test=sc.transform(x_test)

#Lojistik Regresyon
from sklearn.linear_model import LogisticRegression
logr= LogisticRegression(random_state=0)
logr.fit(X_train,y_train)
logrp=logr.predict(X_test)
cm1= confusion_matrix(y_test,logrp)
print("Lojistik Regresyon")
print(cm1)

#KNN
from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors=5, metric="minkowski")
knn.fit(X_train, y_train)
knnp=knn.predict(X_test)
cm2= confusion_matrix(y_test,knnp)
print("KNN")
print(cm2)

#Destek Vektör 
from sklearn.svm import SVC
svc= SVC(kernel="poly")
svc.fit(X_train,y_train)
svcp=svc.predict(X_test)
cm3= confusion_matrix(y_test,svcp)
print("Destek Vektör")
print(cm3)

#Naive Bayes
from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(X_train, y_train)
gnbp=gnb.predict(X_test)
cm4= confusion_matrix(y_test,gnbp)
print("Naive Bayes")
print(cm4)

#Karar Ağacı
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(criterion="entropy")
dtc.fit(X_train,y_train)
dtcp=dtc.predict(X_test)
cm5= confusion_matrix(y_test,dtcp)
print("Karar Ağacı")
print(cm5)

#Rassal Orman
from sklearn.ensemble import RandomForestClassifier
rfc= RandomForestClassifier(n_estimators=6, criterion="entropy")
rfc.fit(X_train, y_train)
rfcp=rfc.predict(X_test)
cm6= confusion_matrix(y_test,rfcp)
print("Rassal Orman")
print(cm6)

#ROC and AUC
from sklearn import metrics
rfcp2= rfc.predict_proba(X_test)
fpr,tpr,thresholds=metrics.roc_curve(y_test, rfcp2[:,0], pos_label="e")
print(y_test)
print(rfcp2)
print(tpr)
print(fpr)


