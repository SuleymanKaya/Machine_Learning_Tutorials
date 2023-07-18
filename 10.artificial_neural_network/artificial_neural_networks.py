# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 12:21:54 2019

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

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)

#Yapay Sinir Ağı Oluşturma
from keras.models import Sequential
from keras.layers import Dense

classifier = Sequential()

classifier.add(Dense(6, init="uniform", activation="relu", input_dim=11))
classifier.add(Dense(6, init="uniform", activation="relu"))
classifier.add(Dense(1, init="uniform", activation="sigmoid"))
classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

classifier.fit(x_train, y_train, epochs=40)
y_pred= classifier.predict(x_test)
y_pred= (y_pred > 0.5)

#Sonuçları Değerlendirme
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test, y_pred)
print(cm)
