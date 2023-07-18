# -*- coding: utf-8 -*
"""
Created on Sat Apr  6 15:18:02 2019

@author: suleyman.kaya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


veriler=pd.read_csv('musteriler.csv')

X=veriler.iloc[:,3:].values

from sklearn.cluster import AgglomerativeClustering
ac= AgglomerativeClustering(n_clusters=4, affinity="euclidean", linkage="ward")
Y_tahmin=ac.fit_predict(X)
print(Y_tahmin)

plt.scatter(X[Y_tahmin==0,0],X[Y_tahmin==0,1],s=100, color="red")
plt.scatter(X[Y_tahmin==1,0],X[Y_tahmin==1,1],s=100, color="blue")
plt.scatter(X[Y_tahmin==2,0],X[Y_tahmin==2,1],s=100, color="green")
plt.scatter(X[Y_tahmin==3,0],X[Y_tahmin==3,1],s=100, color="grey")
plt.title("HC")
plt.show()

import scipy.cluster.hierarchy as sch
dendrogram=sch.dendrogram(sch.linkage(X, method="ward"))
plt.title("Dendogram")
plt.show()

