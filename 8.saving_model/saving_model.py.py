# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:36:23 2019

@author: suleyman.kaya
"""

import pandas as pd

veriler= pd.read_csv("satislar.csv")

x= veriler.iloc[:,0:1]
y= veriler.iloc[:,1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, train_size=0.67)

"""
from sklearn.linear_model import LinearRegression
lr= LinearRegression()
lr.fit(x_train, y_train)"""

import pickle as pck

dosya= "Model_Dosyası-1"
#pck.dump(lr, open(dosya, "wb"))
yuklenen= pck.load(open(dosya,"rb"))
print(yuklenen.predict(x_test))


