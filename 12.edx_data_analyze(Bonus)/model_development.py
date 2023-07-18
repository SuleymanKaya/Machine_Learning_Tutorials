# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:49:04 2019

@author: suleyman.kaya
"""

import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/automobileEDA.csv'
Tum_Data = pd.read_csv(path)

from sklearn.linear_model import LinearRegression
lr= LinearRegression()

x = Tum_Data[['highway-mpg']]
y = Tum_Data['price']

lr.fit(x,y)
ypred= lr.predict(x)
kesişim= lr.intercept_
eğim= lr.coef_

width= 6
height= 5
plt.figure(figsize=(width, height))

sns.regplot(x=x, y=y, data=Tum_Data) #verilerin arasındaki ilişkiyi gösteren grafik
plt.show()

sns.residplot(x, y)
plt.show()

ax1= sns.distplot(Tum_Data["price"], hist=False, color="r", label="Gerçek Değer")
sns.distplot(ypred, hist=False, color="b", label="Tahmin Edilen", ax=ax1)
plt.title('Fiyat İçin Gerçek ve Tahmin Edilen Değerler')
plt.xlabel('Fiyat($)')
plt.ylabel('Arabaların Oranı')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
pr= PolynomialFeatures(degree=5)
x_pr= pr.fit_transform(x)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe= Pipeline([('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)), ('model',LinearRegression())])
pipe.fit(x_pr, y)
ypipe= pipe.predict(x_pr)


from sklearn.metrics import mean_squared_error

mse1= mean_squared_error(y,ypred)
R_squared1= lr.score(x,y)

mse2= mean_squared_error(y,ypipe)
R_squared2= pipe.score(x_pr, y)

