# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:10:43 2019

@author: suleyman.kaya
"""

import pandas as pd

veriler = pd.read_csv('KacanMusteri.csv')

X=veriler.iloc[:,3:13].values
Y=veriler.iloc[:,13].values

#Veri Ön İşleme
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

X[:,1]=le.fit_transform(X[:,1])
X[:,2]=le.fit_transform(X[:,2])

from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder(categorical_features=[1]) 
X=ohe.fit_transform(X).toarray()
X=X[:,1:]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size=0.67, random_state=0)

from xgboost import XGBClassifier
xgbt= XGBClassifier()
xgbt.fit(x_train, y_train)
y_pred= xgbt.predict(x_test)

from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test, y_pred)
print(cm)
