# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 17:44:46 2019

@author: suleyman.kaya
"""

import pandas as pd



path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/module_5_auto.csv'
Tum_Data = pd.read_csv(path)
Tum_Data2= Tum_Data._get_numeric_data()

y_data= Tum_Data2["price"]
x_data= Tum_Data2.drop("price", axis=1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.25, random_state=0)

from sklearn.linear_model import LinearRegression
lr= LinearRegression()
lr.fit(x_train[["horsepower"]], y_train)
R_square1= lr.score(x_test[["horsepower"]], y_test)

from sklearn.model_selection import cross_val_score, cross_val_predict
R_cross1 = cross_val_score(estimator=lr, X=x_data[['horsepower']], y=y_data, cv=4)
mean_square_error1= -1 * cross_val_score(lr, x_data[['horsepower']], y_data, cv=4, scoring='neg_mean_squared_error')
Y_cross_pred1= cross_val_predict(lr, X=x_data[['horsepower']], y=y_data, cv=4)

from sklearn.preprocessing import PolynomialFeatures
pr=PolynomialFeatures(degree=3)
x_train_pr=pr.fit_transform(x_train[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])
x_test_pr=pr.fit_transform(x_test[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg','normalized-losses','symboling']])

from sklearn.linear_model import Ridge
Ridge_Model= Ridge(alpha=0.1)
Ridge_Model.fit(x_train_pr, y_train)
y_ridge_pred1= Ridge_Model.predict(x_test_pr)

from sklearn.model_selection import GridSearchCV
parameters1= [{'alpha': [0.001,0.1,1, 10, 100, 1000, 10000, 100000, 100000], 'normalize':[True,False]}]
Ridge2= Ridge()
Grid1= GridSearchCV(Ridge2, parameters1, cv=4)
Grid1.fit(x_train_pr, y_train)
Best_Param= Grid1.best_params_

